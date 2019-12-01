import urwid
import pymongo
from can_message_type import can_msg_types

import threading, logging
from time import sleep
import time

class interface(object):
    def __init__(self, debug = False):
        self.debug = debug
        self.palette =[
                       ('titlebar', 'dark red', ''),
                       ('quit button', 'dark red', ''),
                       ('headers', 'white,bold', ''),
                       ('change', 'dark green, bold', ''),
                       ('id', 'brown', ''),
                       ('unchanged', 'dark gray', '')]

        self.header_text = urwid.Text(u' UTSME19 Telemetry')
        self.header = urwid.AttrMap(self.header_text, 'titlebar')

        self.menu = urwid.Text([u'Press (', ('quit button', u'Q'), u') to quit.'])


        # Start the dB interface
        self.client = pymongo.MongoClient("mongodb://localhost:27020/")
        self.database = self.client["UTSM19-" + time.strftime("%Y-%m-%d")]

        # Get the can message table interpreter
        self.can_interpret = can_msg_types()
        self.can_table = self.can_interpret.get_can_table()

        # Create the start screen
        self.start_text = urwid.Text(u'Press (S) to begin telemetry system')
        self.start_filler = urwid.Filler(self.start_text, valign='top', top=1, bottom=1)
        self.v_padding = urwid.Padding(self.start_filler, left=1, right=1)
        self.start_box = urwid.LineBox(self.v_padding)

        # Assemble the widgets
        self.layout = urwid.Frame(header=self.header, body=self.start_box, footer=self.menu)

        # Start the dB thread
        self.db_thread = threading.Thread(target=self.readfromDB)
        self.db_thread.start()


    # Handle key presses
    def handle_input(self, key):
        if key == 'S' or key == 's':
            self.refresh_screen(self.main_loop, '')

        if key == 'Q' or key == 'q':
            raise urwid.ExitMainLoop()
    
    def append_text(self, base_text, added_text, tabsize=10, color='white'):
        base_text.append((color, added_text.expandtabs(tabsize)))
    
    def append_header (self, base_text, added_text, color='white'):
        base_text.append((color, added_text))

    def update_screen(self):
        updates = []
        for id, data in self.can_table.items():
            #print("The Current ID Name is: " + id)
            header = [('headers', u'Can ID\t'.expandtabs(14))]
            self.append_header(updates, header)
            for key in data:
                if key is not "Timestamp":
                    text = '{} \t'.format(key)
                    header = ('headers', text.expandtabs(9))
                else:
                    text = '\t{}'.format(key)
                    header = ('headers', text.expandtabs(7))

                
                self.append_header(updates, header)
                #print(updates)

            self.append_text(updates, u'\n', tabsize=0)
            self.append_text(updates, '{} \t'.format(id), tabsize=17, color="id")
            
            for key in data:
                if key is not "Timestamp":
                    self.append_text(updates, '{0:.2f} \t'.format(data[key]), tabsize=18, color=self.get_color(id, key))
                else:
                    self.append_text(updates, '{} \t'.format(data[key]), tabsize=17, color=self.get_color(id, key))

            self.append_text(updates, u' \n', tabsize=0)
        # print(updates)
        self.can_interpret.update_previous_db()
        return updates

    def get_color(self, id, key):
        comparator = self.can_interpret.compare_database(id, key)

        if comparator is True:
            color = 'unchanged'
        elif comparator is False:
            color = 'change'
        return color

    def readfromDB(self):
        change_stream = self.database.watch()
        for change in change_stream:
            id_name = change["ns"]["coll"]
            data = change["fullDocument"]
            del data["_id"]
            self.can_table = self.can_interpret.set_db_data(id_name, data)

    def refresh_screen(self, _loop, _data):
        self.main_loop.draw_screen()
        #data = self.readfromDB()
        self.start_box.base_widget.set_text(self.update_screen())
        self.main_loop.set_alarm_in(0.04, self.refresh_screen)

    def start_screen(self):
        # Start the main loop
        self.main_loop = urwid.MainLoop(self.layout, self.palette, unhandled_input=self.handle_input)
        self.main_loop.set_alarm_in(0, self.refresh_screen)
        self.main_loop.run()

 





