
# import scapy.all as scapy
# import json

# packet_list = []

# def sniff(interface):
#     scapy.sniff(iface=interface, store=False, prn=process_packet)

# def process_packet(packet):
#     packet_dict = {
#         'timestamp': str(packet.time),
#         'source': packet.src,
#         'destination': packet.dst,
#         'summary': packet.summary(),
#         'raw': str(packet.payload)
#         # Add more fields as needed
#     }
#     packet_list.append(packet_dict)
#     save_to_json(packet_list)

# def save_to_json(packet_list):
#     with open('captured_packets.json', 'w') as json_file:
#         json.dump(packet_list, json_file, indent=2)

# # Replace 'eth0' with the name of your LAN interface
# sniff('eth0')

# import tkinter as tk

# root = tk.Tk()

# label = tk.Label(root, text="Hello, Tkinter!")
# label.pack()

# root.mainloop()
# from PyQt5.QtWidgets import QApplication, QLabel

# app = QApplication([])

# label = QLabel('Hello, PyQt!')
# label.show()

# app.exec_()
# from kivy.app import App
# from kivy.uix.button import Button

# class MyApp(App):
#     def build(self):
#         return Button(text='Hello, Kivy!')

# MyApp().run()

# import wx

# app = wx.App(False)
# frame = wx.Frame(None, wx.ID_ANY, "Hello, wxPython!")
# frame.Show(True)

# app.MainLoop()