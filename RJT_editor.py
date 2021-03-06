# coding:UTF-8
import threading
import tempfile
import os
import json
import zipfile
VERSION = '1.1'
TYPE = 'EXE'


try:
    import tkinter as tk
    from tkinter import Checkbutton, ttk, font as tkFont
    from tkinter.colorchooser import askcolor
    from tkinter import messagebox
    from PIL import Image, ImageDraw
    import requests
    import re
except:
    os.system('pip install tkinter')
    os.system('pip install pillow')
    os.system('pip install requests')
    import tkinter as tk
    import re
    from tkinter import Checkbutton, font as tkFont
    from tkinter import ttk
    from tkinter.colorchooser import askcolor
    from tkinter import messagebox
    from PIL import Image, ImageDraw
try:
    import pyperclip
except:
    os.system('pip install pyperclip')
    import pyperclip
try:
    os.remove('newVersion/README.md')
    os.remove('newVersion/RJT_editor.py')
    os.removedirs('newVersion')
    os.remove('newVersion.zip')
except:
    pass
try:
    with open('Temp/RJT_ver') as f:
        print(f.read())
        os.remove('Temp/RJT_ver')
except:
    pass
try:
    os.remove('newVersion.exe')
except:
    pass
try:
    os.remove('newVersion.py')
except:
    pass
try:
    os.remove('newVersion.zip')
except:
    pass


def drawIcon():
    w = 32
    h = 32
    icon = [(162, 163, 163), (161, 161, 161), (160, 160, 160), (159, 159, 160), (158, 157, 158), (156, 157, 156), (155, 155, 155), (154, 154, 154), (153, 152, 153), (151, 151, 152), (149, 151, 150), (149, 149, 149), (147, 147, 148), (146, 146, 147), (145, 145, 145), (145, 143, 144), (143, 143, 143), (142, 142, 141), (140, 141, 140), (139, 139, 139), (138, 139, 138), (138, 138, 137), (136, 137, 137), (136, 136, 135), (135, 135, 135), (135, 134, 135), (134, 134, 133), (134, 135, 133), (134, 135, 134), (135, 135, 135), (136, 135, 135), (136, 136, 136), (163, 162, 162), (161, 162, 160), (161, 160, 159), (159, 158, 159), (157, 157, 157), (156, 156, 156), (155, 155, 155), (154, 153, 154), (153, 152, 153), (151, 151, 151), (149, 150, 149), (149, 148, 149), (147, 147, 147), (146, 145, 146), (145, 144, 145), (144, 143, 144), (142, 142, 142), (140, 141, 141), (140, 140, 140), (139, 139, 139), (138, 137, 138), (137, 136, 137), (136, 135, 136), (135, 135, 135), (135, 133, 134), (133, 133, 133), (132, 134, 132), (133, 133, 133), (133, 133, 133), (134, 133, 133), (134, 134, 135), (135, 135, 135), (162, 162, 162), (161, 161, 161), (241, 241, 242), (240, 240, 240), (240, 239, 239), (239, 238, 239), (237, 237, 238), (237, 236, 237), (235, 236, 236), (235, 234, 234), (234, 234, 233), (232, 233, 232), (232, 232, 232), (231, 231, 231), (230, 230, 230), (230, 229, 229), (228, 228, 228), (227, 228, 227), (227, 226, 227), (225, 226, 225), (224, 224, 224), (224, 224, 224), (224, 224, 224), (224, 224, 224), (224, 224, 224), (224, 224, 224), (224, 224, 224), (224, 224, 224), (224, 224, 224), (224, 224, 224), (133, 133, 133), (135, 134, 134), (162, 163, 162), (161, 161, 161), (242, 242, 242), (241, 242, 241), (241, 240, 239), (240, 239, 239), (238, 238, 238), (237, 238, 237), (236, 236, 236), (235, 235, 235), (235, 234, 235), (234, 233, 234), (233, 233, 232), (232, 231, 231), (202, 202, 202), (134, 134, 134), (131, 131, 131), (226, 226, 225), (227, 228, 227), (226, 226, 226), (226, 225, 225), (224, 224, 224), (224, 224, 224), (224, 224, 224), (224, 224, 224), (224, 224, 224), (224, 224, 224), (224, 224, 224), (224, 224, 224), (224, 224, 224), (132, 132, 132), (133, 133, 134), (162, 162, 162), (161, 161, 160), (243, 242, 243), (241, 241, 242), (229, 229, 228), (180, 180, 180), (148, 149, 148), (140, 140, 140), (145, 145, 145), (160, 160, 160), (179, 178, 178), (193, 193, 193), (197, 197, 197), (182, 182, 182), (138, 138, 138), (130, 130, 130), (131, 131, 131), (157, 156, 156), (193, 192, 193), (194, 194, 194), (184, 184, 184), (170, 170, 170), (156, 156, 156), (144, 144, 144), (137, 137, 137), (143, 143, 143), (160, 160, 160), (204, 204, 204), (224, 224, 224), (224, 224, 224), (131, 132, 132), (132, 133, 133), (162, 162, 162), (160, 161, 160), (243, 243, 243), (235, 235, 236), (149, 149, 149), (132, 132, 132), (130, 130, 130), (132, 131, 132), (134, 134, 134), (131, 131, 131), (131, 131, 131), (131, 131, 131), (131, 131, 131), (131, 131, 131), (136, 136, 136), (192, 191, 191), (158, 158, 158), (129, 129, 129), (131, 131, 131), (131, 131, 131), (131, 131, 131), (131, 131, 131), (131, 131, 131), (132, 132, 132), (130, 130, 130), (130, 130, 130), (131, 131, 131), (135, 135, 135), (201, 201, 201), (224, 224, 224), (131, 132, 131), (132, 133, 133), (162, 162, 162), (161, 161, 161), (244, 244, 244), (193, 194, 193), (134, 134, 134), (137, 137, 137), (199, 199, 199), (239, 240, 239), (238, 239, 238), (227, 227, 226), (198, 198, 198), (180, 179, 180), (172, 172, 172), (203, 203, 203), (231, 232, 232), (232, 225, 225), (231, 230, 231), (216, 216, 216), (172, 171, 171), (170, 170, 170), (184, 184, 185), (205, 205, 205), (221, 221, 221), (224, 225, 224), (224, 224, 224), (184, 184, 184), (136, 136, 136), (132, 132, 132), (144, 144, 144), (224, 224, 224), (131, 131, 132), (133, 132, 132), (163, 162, 162), (160, 161, 161), (245, 244, 245), (170, 170, 170), (133, 133, 133), (145, 145, 145), (241, 241, 241), (240, 240, 240), (239, 239, 239), (238, 238, 239), (238, 237, 238), (236, 237, 236), (235, 235, 236), (234, 234, 235), (234, 233, 234), (232, 233, 232), (232, 231, 231), (231, 231, 230), (230, 230, 229), (230, 229, 228), (228, 228, 227), (226, 227, 227), (226, 226, 226), (225, 225, 225), (223, 225, 224), (224, 224, 224), (144, 144, 144), (132, 132, 132), (130, 130, 130), (224, 224, 224), (131, 131, 132), (133, 134, 132), (163, 162, 162), (161, 161, 161), (245, 246, 245), (169, 169, 168), (146, 146, 146), (161, 161, 161), (242, 241, 242), (241, 241, 241), (240, 240, 240), (239, 239, 239), (237, 238, 237), (237, 233, 233), (237, 207, 208), (243, 118, 124), (247, 68, 75), (239, 159, 162), (223, 231, 223), (137, 217, 127), (112, 214, 99), (165, 221, 158), (207, 226, 206), (223, 227, 222), (223, 226, 224), (225, 225, 225), (225, 225, 224), (224, 224, 224), (161, 161, 161), (145, 145, 145), (145, 145, 145), (224, 224, 224), (132, 133, 132), (134, 133, 133), (162, 162, 163), (161, 160, 161), (245, 246, 247), (238, 238, 238), (237, 237, 237), (237, 238, 237), (242, 242, 243), (241, 242, 241), (241, 237, 238), (240, 223, 223), (240, 180, 183), (246, 90, 96), (250, 16, 27), (251, 0, 12), (251, 5, 16), (243, 107, 113), (203, 225, 197), (89, 218, 73), (23, 207, 0), (23, 204, 0), (30, 204, 8), (58, 207, 40), (103, 212, 90), (147, 217, 140), (205, 224, 203), (225, 225, 224), (195, 217, 192), (219, 218, 220), (218, 218, 218), (224, 224, 224), (133, 133, 133), (134, 133, 135), (162, 162, 163), (160, 162, 161), (246, 247, 246), (245, 246, 246), (244, 245, 245), (244, 244, 245), (242, 243, 243), (242, 242, 242), (243, 188, 190), (249, 59, 67), (251, 7, 18), (251, 0, 12), (251, 0, 12), (251, 0, 12), (252, 0, 12), (248, 64, 72), (180, 184, 132), (66, 214, 51), (23, 206, 0), (23, 204, 0), (23, 204, 0), (23, 204, 0), (23, 204, 0), (23, 207, 0), (47, 205, 29), (226, 225, 225), (208, 222, 207), (224, 224, 224), (224, 224, 224), (224, 224, 224), (134, 134, 134), (134, 136, 135), (163, 163, 163), (161, 162, 161), (248, 248, 247), (247, 247, 247), (246, 245, 246), (245, 245, 245), (244, 244, 244), (242, 242, 243), (244, 168, 171), (251, 19, 29), (252, 0, 12), (251, 0, 12), (251, 0, 12), (251, 0, 12), (251, 0, 12), (249, 24, 34), (162, 137, 66), (47, 211, 31), (22, 205, 0), (23, 204, 0), (23, 204, 0), (23, 204, 0), (23, 204, 0), (23, 210, 0), (88, 210, 73), (226, 226, 226), (216, 224, 215), (224, 224, 224), (224, 224, 224), (224, 224, 224), (135, 136, 135), (136, 136, 137), (163, 163, 164), (162, 162, 161), (248, 248, 248), (248, 247, 248), (247, 246, 247), (246, 245, 245), (244, 244, 245), (243, 244, 244), (243, 211, 213), (249, 71, 77), (253, 0, 12), (251, 0, 12), (251, 0, 12), (251, 0, 12), (251, 0, 12), (247, 4, 13), (139, 109, 17), (27, 207, 10), (22, 204, 0), (23, 204, 0), (23, 204, 0), (23, 204, 0), (23, 204, 0), (23, 212, 0), (124, 215, 113), (226, 227, 227), (225, 226, 225), (225, 224, 225), (224, 224, 224), (224, 224, 224), (137, 136, 136), (137, 137, 137), (163, 163, 163), (162, 162, 162), (249, 249, 249), (248, 248, 248), (247, 248, 246), (245, 247, 246), (245, 245, 246), (244, 244, 244), (244, 241, 242), (247, 124, 129), (253, 7, 18), (251, 0, 12), (251, 0, 11), (247, 0, 14), (231, 0, 24), (211, 14, 26), (108, 120, 9), (19, 207, 0), (23, 204, 0), (23, 204, 0), (23, 204, 0), (23, 204, 0), (23, 204, 0), (23, 212, 0), (160, 219, 154), (227, 227, 227), (226, 227, 226), (225, 225, 226), (224, 225, 224), (224, 224, 224), (137, 138, 137), (139, 138, 139), (163, 164, 163), (162, 162, 162), (250, 250, 250), (249, 248, 249), (247, 248, 248), (248, 246, 247), (247, 245, 247), (246, 244, 245), (245, 242, 244), (245, 177, 179), (251, 37, 46), (253, 0, 12), (251, 0, 11), (232, 2, 24), (151, 5, 77), (91, 40, 87), (53, 145, 27), (21, 206, 0), (23, 204, 0), (23, 204, 0), (23, 204, 0), (23, 204, 0), (23, 205, 0), (33, 207, 12), (184, 222, 179), (228, 227, 229), (227, 227, 227), (226, 226, 227), (225, 226, 225), (224, 224, 224), (140, 138, 139), (139, 139, 139), (164, 164, 165), (163, 163, 163), (250, 251, 250), (249, 249, 250), (249, 248, 249), (247, 248, 247), (247, 247, 246), (246, 245, 246), (246, 244, 245), (244, 218, 220), (249, 79, 86), (251, 0, 12), (251, 0, 10), (214, 6, 36), (81, 17, 129), (6, 63, 129), (18, 166, 35), (23, 205, 0), (23, 204, 0), (23, 204, 0), (23, 204, 0), (23, 204, 0), (23, 208, 0), (62, 208, 45), (198, 225, 195), (228, 229, 228), (228, 228, 228), (227, 227, 226), (225, 226, 226), (225, 225, 225), (140, 140, 140), (140, 141, 140), (165, 165, 164), (163, 163, 163), (252, 251, 250),
            (250, 250, 250), (250, 249, 249), (248, 248, 249), (247, 247, 248), (246, 246, 246), (245, 245, 246), (244, 237, 236), (247, 131, 137), (250, 27, 37), (249, 60, 68), (200, 89, 122), (60, 43, 165), (5, 48, 145), (11, 114, 82), (15, 151, 49), (18, 173, 28), (21, 194, 8), (22, 203, 0), (23, 204, 0), (23, 210, 0), (92, 213, 79), (211, 227, 210), (230, 229, 229), (228, 229, 228), (227, 229, 227), (227, 227, 227), (226, 226, 225), (141, 142, 141), (141, 142, 142), (165, 164, 165), (165, 164, 164), (252, 252, 252), (250, 251, 251), (250, 250, 250), (249, 249, 249), (248, 248, 248), (248, 247, 247), (246, 246, 246), (245, 243, 243), (245, 205, 206), (246, 158, 161), (244, 188, 191), (185, 178, 216), (40, 53, 186), (1, 19, 172), (2, 32, 160), (4, 53, 141), (6, 71, 122), (8, 92, 102), (11, 115, 83), (33, 157, 64), (50, 203, 37), (136, 219, 127), (224, 230, 223), (230, 231, 230), (230, 229, 229), (229, 228, 228), (228, 227, 227), (226, 227, 227), (142, 142, 143), (143, 143, 144), (166, 166, 165), (164, 165, 164), (252, 252, 252), (252, 252, 251), (251, 250, 251), (250, 249, 250), (249, 248, 249), (248, 248, 247), (247, 247, 247), (245, 246, 246), (246, 244, 243), (245, 243, 244), (243, 243, 243), (175, 179, 224), (21, 36, 180), (1, 17, 175), (0, 17, 175), (0, 17, 175), (0, 16, 175), (0, 18, 173), (1, 28, 168), (66, 104, 166), (160, 209, 167), (205, 229, 202), (233, 231, 231), (232, 231, 231), (229, 230, 230), (229, 229, 229), (228, 229, 228), (227, 227, 227), (143, 144, 143), (145, 144, 144), (166, 166, 166), (166, 164, 165), (252, 252, 252), (252, 252, 252), (251, 252, 251), (251, 250, 251), (249, 250, 250), (248, 249, 249), (248, 247, 248), (247, 246, 246), (246, 246, 245), (245, 245, 245), (242, 241, 244), (166, 170, 221), (13, 28, 178), (0, 17, 175), (0, 17, 175), (0, 17, 175), (0, 17, 175), (0, 17, 175), (0, 17, 179), (92, 102, 199), (217, 217, 230), (234, 233, 234), (232, 233, 232), (231, 231, 232), (231, 230, 231), (230, 230, 229), (229, 229, 228), (228, 228, 228), (145, 145, 145), (146, 145, 145), (166, 166, 166), (165, 166, 166), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 251, 250), (250, 250, 251), (249, 250, 249), (248, 249, 248), (247, 248, 247), (246, 246, 247), (246, 246, 245), (236, 237, 241), (149, 154, 217), (11, 26, 178), (0, 17, 175), (0, 17, 175), (0, 17, 175), (0, 17, 175), (0, 17, 175), (4, 20, 177), (106, 116, 202), (219, 221, 231), (234, 235, 234), (234, 233, 233), (232, 232, 233), (232, 232, 231), (230, 231, 230), (229, 230, 229), (228, 229, 228), (146, 147, 147), (147, 147, 146), (166, 166, 166), (166, 166, 166), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 251, 251), (251, 250, 252), (250, 250, 249), (249, 249, 249), (248, 248, 249), (247, 247, 247), (246, 246, 247), (229, 231, 240), (129, 136, 211), (9, 24, 177), (0, 17, 175), (0, 17, 175), (0, 17, 175), (0, 17, 175), (0, 17, 176), (14, 29, 178), (124, 132, 207), (223, 223, 232), (234, 235, 235), (234, 234, 234), (233, 233, 233), (232, 232, 232), (232, 231, 231), (230, 231, 230), (229, 229, 229), (148, 147, 148), (148, 148, 148), (166, 166, 166), (166, 166, 166), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 252, 251), (251, 250, 251), (249, 249, 250), (249, 249, 248), (248, 248, 248), (247, 247, 246), (232, 234, 242), (165, 170, 221), (88, 98, 200), (55, 67, 190), (26, 41, 181), (6, 23, 176), (0, 17, 175), (0, 17, 176), (24, 38, 181), (143, 149, 213), (226, 228, 233), (235, 236, 235), (235, 235, 234), (234, 234, 234), (233, 233, 233), (232, 232, 232), (230, 231, 231), (231, 230, 230), (149, 149, 148), (149, 149, 150), (166, 166, 166), (166, 166, 166), (252, 252, 252), (166, 166, 166), (133, 133, 133), (147, 147, 147), (252, 252, 252), (252, 251, 251), (250, 250, 251), (249, 250, 249), (249, 248, 249), (247, 248, 247), (245, 246, 246), (239, 240, 244), (232, 234, 241), (227, 229, 238), (224, 225, 237), (211, 212, 234), (183, 188, 225), (149, 154, 214), (137, 143, 211), (194, 194, 225), (233, 233, 235), (237, 237, 235), (235, 236, 235), (234, 234, 234), (154, 154, 153), (130, 130, 130), (131, 131, 131), (230, 231, 231), (150, 150, 150), (151, 150, 150), (166, 166, 166), (166, 166, 166), (252, 252, 252), (175, 175, 175), (133, 133, 133), (147, 147, 147), (252, 252, 252), (252, 251, 252), (251, 251, 251), (250, 250, 250), (249, 250, 249), (247, 248, 249), (248, 247, 247), (247, 246, 246), (245, 245, 245), (244, 245, 245), (243, 244, 244), (243, 243, 242), (241, 241, 241), (239, 239, 239), (238, 238, 239), (237, 238, 237), (237, 238, 238), (237, 236, 237), (235, 237, 236), (235, 235, 235), (146, 146, 146), (131, 131, 131), (131, 131, 131), (232, 231, 231), (151, 152, 152), (152, 152, 151), (166, 166, 166), (166, 166, 166), (252, 252, 252), (203, 203, 203), (134, 134, 134), (135, 135, 135), (179, 179, 179), (215, 215, 215), (221, 220, 220), (194, 195, 196), (170, 169, 170), (153, 153, 153), (148, 148, 148), (172, 172, 172), (229, 229, 229), (246, 245, 246), (244, 243, 244), (183, 183, 183), (149, 149, 149), (150, 150, 150), (158, 159, 159), (179, 178, 178), (202, 201, 201), (206, 206, 205), (197, 196, 197), (159, 159, 159), (133, 133, 133), (132, 132, 132), (149, 149, 149), (231, 232, 232), (153, 153, 153), (152, 153, 152), (166, 166, 166), (166, 166, 166), (252, 252, 252), (251, 251, 251), (161, 161, 161), (133, 133, 133), (131, 131, 131), (131, 131, 131), (131, 131, 131), (131, 131, 131), (131, 131, 131), (131, 131, 131), (131, 131, 131), (131, 131, 131), (133, 133, 133), (184, 184, 184), (150, 150, 150), (132, 132, 132), (131, 131, 131), (131, 131, 131), (131, 131, 131), (131, 131, 131), (131, 131, 131), (131, 131, 131), (131, 131, 131), (131, 131, 131), (132, 132, 132), (139, 139, 139), (217, 217, 217), (232, 233, 233), (153, 155, 153), (154, 155, 154), (166, 166, 166), (166, 166, 166), (252, 252, 252), (252, 252, 252), (249, 249, 249), (207, 207, 207), (170, 170, 170), (162, 162, 162), (165, 165, 165), (179, 179, 179), (198, 198, 198), (215, 215, 215), (223, 223, 224), (208, 208, 208), (152, 152, 152), (130, 130, 130), (131, 131, 131), (166, 166, 166), (216, 216, 215), (219, 219, 219), (205, 204, 205), (189, 189, 189), (173, 173, 173), (162, 162, 162), (157, 157, 157), (161, 161, 161), (181, 182, 182), (228, 228, 229), (235, 234, 235), (233, 233, 234), (155, 156, 156), (156, 156, 155), (166, 166, 166), (166, 166, 166), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 252, 253), (251, 251, 251), (250, 250, 250), (249, 249, 249), (222, 222, 221), (147, 147, 147), (147, 147, 147), (246, 246, 245), (245, 245, 244), (244, 244, 244), (243, 243, 242), (241, 242, 241), (241, 240, 240), (240, 240, 239), (239, 239, 238), (238, 238, 237), (237, 237, 236), (235, 236, 236), (236, 234, 235), (235, 234, 235), (156, 156, 157), (157, 157, 157), (166, 166, 166), (166, 166, 166), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 252, 252), (252, 252, 252), (253, 252, 251), (251, 251, 250), (250, 250, 249), (249, 248, 249), (248, 248, 248), (247, 246, 248), (246, 245, 247), (245, 246, 245), (244, 244, 245), (244, 243, 243), (242, 242, 243), (241, 241, 242), (240, 241, 240), (239, 239, 240), (240, 238, 238), (237, 238, 237), (237, 236, 237), (235, 236, 236), (235, 234, 235), (157, 159, 157), (158, 157, 158), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (165, 166, 165), (165, 166, 164), (164, 164, 165), (163, 163, 164), (163, 163, 163), (162, 163, 163), (162, 162, 162), (161, 161, 161), (161, 161, 161), (161, 160, 160), (160, 160, 160), (161, 160, 159), (160, 160, 159), (159, 159, 159), (159, 160, 158), (159, 160, 159), (159, 159, 158), (159, 159, 158), (159, 159, 159), (159, 159, 158), (159, 159, 159), (159, 160, 159), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 166, 166), (166, 165, 165), (165, 165, 164), (164, 163, 164), (163, 164, 164), (163, 164, 163), (163, 163, 163), (162, 163, 162), (162, 161, 163), (161, 162, 161), (160, 161, 161), (161, 161, 161), (160, 161, 160), (161, 160, 161), (161, 160, 160), (160, 160, 161), (160, 161, 160), (160, 160, 161), (161, 160, 161), (161, 160, 160), (161, 160, 161)]
    image = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    i = 0
    for x in range(w):
        for y in range(h):
            draw.point((x, y), fill=icon[i])
            i = i+1
    image.save(tempfile.gettempdir()+'RJTeditorIcon.ico', 'ico')
    image.close()
    del draw


drawIcon()


text = ''
color = ''
font_ = ''
bold = False
italic = False
underlined = False
strikethrough = False
obfuscated = False
clickEvent = {'action': '', 'value': ''}
hoverEvent = {'action': '', 'contents': ''}
outPut = {}


def setEmpty(row_, column_, width_=10, height_=10, sep_=True):
    empty = tk.Canvas(width=width_, height=height_)
    empty.grid(row=row_, column=column_)
    if sep_ == True:
        sep = tk.Canvas(bg="dark gray", height=1)
        sep.grid(row=row_, column=column_, columnspan=3, sticky='we')


def choose_color_(event):
    global choose_color, color_get
    if choose_color.get() == '-[???????????????]-':
        color_get = str(askcolor(title='????????????')[1])
        if '#' not in str(color_get):
            choose_color.set('??????')
            color_get = 'white'
        else:
            choose_color.set('-[???????????????]-:'+color_get)
    else:
        color_get = {'??????': 'black', '??????': 'white', '?????????': 'dark_blue', '?????????': 'blue', '?????????': 'dark_green', '?????????': 'green', '?????????': 'dard_aqua', '?????????': 'aqua',
                     '?????????': 'dark_red', '?????????': 'red', '?????????': 'purple', '?????????': 'light_purple', '??????': 'gold', '??????': 'gray', '?????????': 'dark_gray', '??????': 'yellow'}[choose_color.get()]


def choose_font_(event):
    global choose_font, font_get
    font_get = {'????????????': 'minecraft:default', '??????unicode??????': 'minecraft:uniform',
                '??????????????????': 'minecraft:alt', 'Dungeons????????????': 'minecraft:illageralt'}[choose_font.get()]


def required_(event):
    required.post(event.x_root, event.y_root)


def setDefault():
    bold_.set(0)
    underlined_.set(0)
    italic_.set(0)
    obfuscated_.set(0)
    strikethrough_.set(0)


def undoDefault():
    if str(bold_.get()) == '1' or str(underlined_.get()) == '1' or str(italic_.get()) == '1' or str(obfuscated_.get()) == '1' or str(strikethrough_.get()) == '1':
        default_.set(0)
        obfuscated_.set(0)


def undoObfuscated():
    bold_.set(0)
    underlined_.set(0)
    italic_.set(0)
    strikethrough_.set(0)
    default_.set(0)


def choose_click_press(*args):
    helpText = {'?????????[??????]????????????': '????????????url', '????????????(???????????????)': '???????????????', '???????????????????????????[??????]': '??????????????????',
                '?????????[??????]???(???????????????)': '??????????????????', '???[??????]??????????????????': '??????????????????'}[ClickEventTypeChoose.get()]
    if helpText == '???????????????':
        tipClick.config(text='??????:  '+helpText)
        ClickEventValue.insert(0, '/')
    else:
        tipClick.config(text='??????:  '+helpText)
        if ClickEventValue.get()[0:1] == '/':
            ClickEventValue.delete(0)


def clickEvent_press():
    if str(useClick.get()) == '0':
        ClickEventTypeChoose['state'] = 'disabled'
        tipClick['state'] = 'disabled'
        ClickEventValue['state'] = 'disabled'
        tipClickEventType['state'] = 'disabled'
    else:
        ClickEventTypeChoose['state'] = 'readonly'
        tipClick['state'] = 'abled'
        ClickEventValue['state'] = 'abled'
        tipClickEventType['state'] = 'abled'


def HoverEvent_press():
    if str(useHover.get()) == '0':
        hoverEventTypeChoose['state'] = 'disabled'
        tipHover['state'] = 'disabled'
        hoverEventValue['state'] = 'disabled'
        tipHoverEventType['state'] = 'disabled'
    else:
        hoverEventTypeChoose['state'] = 'readonly'
        tipHover['state'] = 'abled'
        hoverEventValue['state'] = 'abled'
        tipHoverEventType['state'] = 'abled'


def Spawn():
    global text, color, font_, bold, italic, underlined, strikethrough, obfuscated, clickEvent, hoverEvent, outPut
    raw_font = choose_font.get()
    text = rawString.get()
    color = color_get
    font_ = font_get
    if str(default_.get()) != 'default':
        if str(bold_.get()) == '1':
            bold = True
        if str(italic_.get()) == '1':
            italic = True
        if str(underlined_.get()) == '1':
            underlined = True
        if str(strikethrough_.get()) == '1':
            strikethrough = True
        if str(obfuscated_.get()) == '1':
            obfuscated = True
        outPut = {'text': text, 'color': color, 'font': font_, 'bold': bold, 'italic': italic,
                  'underlined': underlined, 'strikethrough': strikethrough, 'obfuscated': obfuscated}
    else:
        outPut = {'text': text, 'color': color}
    if str(useClick.get()) == '1':
        clickEvent['action'] = {'?????????[??????]????????????': 'open_url', '????????????(???????????????)': 'run_command', '???????????????????????????[??????]': 'suggest_command',
                                '?????????[??????]???(???????????????)': 'change_page', '???[??????]??????????????????': 'copy_to_clipboard'}[ClickEventTypeChoose.get()]
        clickEvent['value'] = ClickEventValue.get()
        outPut.update({'clickEvent': clickEvent})
    if str(useHover.get()) == '1':
        hoverEvent['action'] = {'????????????': 'show_text'}[
            hoverEventTypeChoose.get()]
        hoverEvent['contents'] = hoverEventValue.get()
        outPut.update({'hoverEvent': hoverEvent})
    outPutJson = json.dumps(outPut)
    try:
        pyperclip.copy(outPutJson)
        messagebox.showinfo(title='??????', message='????????????!')
    except:
        messagebox.showerror(title='??????', message='????????????,???????????????!')
    choose_font.set(raw_font)


root = tk.Tk()
root.resizable(False, False)
root.title('RJT editor for Minecraft Java Edition')
root.iconbitmap(tempfile.gettempdir()+'RJTeditorIcon.ico')


tipFont = tkFont.Font(family='??????', size=13)
entryFont = tkFont.Font(family='??????', size=20)

required = tk.Menu(root, tearoff='off')
required.add_command(label='????????????????????????', font=tipFont)


setEmpty(0, 0, sep_=False)

tipClickEventType = ttk.Label(text='???????????????*:', font=tipFont)
tipClickEventType.grid(row=1, column=1, sticky='w')
tipClickEventType.bind('<Enter><Button-3>', required_)

rawString = ttk.Entry(width=31, font=entryFont)
rawString.grid(row=2, column=1, sticky='w,e')

setEmpty(3, 0)
setEmpty(1, 2, sep_=False)

tipClickEventType = ttk.Label(text='????????????*:', font=tipFont)
tipClickEventType.grid(row=4, column=1, sticky='w')
tipClickEventType.bind('<Enter><Button-3>', required_)

colors = tk.StringVar()  # ???????????????????????????????????????
choose_color = ttk.Combobox(
    width=30, textvariable=colors, state='readonly', font=entryFont)  # ?????????
choose_color["values"] = ('??????', '??????', '?????????', '?????????', '?????????',
                          '?????????', '?????????', '?????????', '?????????', '?????????', '?????????', '?????????', '??????', '??????', '?????????', '??????', '-[???????????????]-')
choose_color.current(0)
choose_color.bind('<<ComboboxSelected>>', choose_color_)
choose_color.set('??????')
color_get = 'black'
choose_color.grid(row=5, column=1, sticky='w,e')

setEmpty(6, 0)

tipClickEventType = ttk.Label(text='????????????*:', font=tipFont)
tipClickEventType.grid(row=7, column=1, sticky='w')
tipClickEventType.bind('<Enter><Button-3>', required_)

font_ = tk.StringVar()  # ???????????????????????????????????????
choose_font = ttk.Combobox(width=30, textvariable=font_,
                           state='readonly', font=entryFont)  # ?????????
choose_font["values"] = ('????????????', '??????unicode??????', '??????????????????', 'Dungeons????????????')
choose_font.current(1)
choose_font.bind('<<ComboboxSelected>>', choose_font_)
choose_font.set('????????????')
font_get = 'minecraft:default'
choose_font.grid(row=8, column=1, sticky='w,e')

setEmpty(9, 0)

default_ = tk.StringVar()
default_.set(0)
choose_default = tk.Radiobutton(
    text='??????', font=tipFont, variable=default_, value='default', command=setDefault)
choose_default.grid(row=10, column=1, sticky='w')
default_.set('default')

italic_ = tk.StringVar()
italic_.set(0)
choose_italic = tk.Checkbutton(
    text='??????', font=tipFont, variable=italic_, onvalue=True, offvalue=False, command=undoDefault)
choose_italic.grid(row=10, column=1)

underlined_ = tk.StringVar()
underlined_.set(0)
choose_underlined = tk.Checkbutton(
    text='?????????', font=tipFont, variable=underlined_, onvalue=True, offvalue=False, command=undoDefault)
choose_underlined.grid(row=10, column=1, sticky='e')

strikethrough_ = tk.StringVar()
strikethrough_.set(0)
choose_strikethrough = tk.Checkbutton(
    text='?????????', font=tipFont, variable=strikethrough_, onvalue=True, offvalue=False, command=undoDefault)
choose_strikethrough.grid(row=11, column=1, sticky='e')

bold_ = tk.StringVar()
bold_.set(0)
choose_bold = tk.Checkbutton(
    text='??????', font=tipFont, variable=bold_, onvalue=True, offvalue=False, command=undoDefault)
choose_bold.grid(row=11, column=1)

obfuscated_ = tk.StringVar()
obfuscated_.set(0)
choose_obfuscated = tk.Radiobutton(
    text='????????????', font=tipFont, variable=obfuscated_, value=1, command=undoObfuscated)
choose_obfuscated.grid(row=11, column=1, sticky='w')

setEmpty(12, 0)

useClick = tk.StringVar()
choose_click = Checkbutton(
    text='????????????????????????', font=tipFont, variable=useClick, onvalue=True, offvalue=False, command=clickEvent_press)
choose_click.grid(row=13, column=1, sticky='w')
useClick.set(0)

tipClickEventType = ttk.Label(text='????????????????????????:', font=tipFont)
tipClickEventType.grid(row=14, column=1, sticky='w')
tipClickEventType['state'] = 'disabled'

ClickEventType = tk.StringVar()
ClickEventTypeChoose = ttk.Combobox(
    width=30, textvariable=ClickEventType, state='readonly', font=entryFont)
ClickEventTypeChoose['values'] = (
    '?????????[??????]????????????', '????????????(???????????????)', '???????????????????????????[??????]', '????????????[??????]???(?????????????????????)', '???[??????]??????????????????')
choose_font.current(0)
ClickEventTypeChoose.bind('<<ComboboxSelected>>', choose_click_press)
ClickEventType.set('')
ClickEventTypeChoose['state'] = 'disabled'
ClickEventTypeChoose.set('')
ClickEventTypeChoose.grid(row=15, column=1, sticky='w,e')

tipClick = ttk.Label(text='??????:', font=tipFont)
tipClick.grid(row=16, column=1, sticky='w')
tipClick['state'] = 'disabled'

ClickEventValue = ttk.Entry(width=31, font=entryFont)
ClickEventValue.grid(row=17, column=1, sticky='w,e')
ClickEventValue['state'] = 'disabled'

setEmpty(18, 0)

useHover = tk.StringVar()
choose_Hover = Checkbutton(
    text='????????????????????????', font=tipFont, variable=useHover, onvalue=True, offvalue=False, command=HoverEvent_press)
choose_Hover.grid(row=19, column=1, sticky='w')
useHover.set(0)

tipHoverEventType = ttk.Label(text='????????????????????????:', font=tipFont)
tipHoverEventType.grid(row=20, column=1, sticky='w')
tipHoverEventType['state'] = 'disabled'

hoverEventType = tk.StringVar()
hoverEventTypeChoose = ttk.Combobox(
    width=30, textvariable=hoverEventType, state='disabled', font=entryFont)
hoverEventTypeChoose['values'] = ('????????????')
hoverEventTypeChoose.grid(row=21, column=1, sticky='w,e')
hoverEventType.set('')

tipHover = ttk.Label(text='??????:', font=tipFont)
tipHover.grid(row=22, column=1, sticky='w')
tipHover['state'] = 'disabled'

hoverEventValue = ttk.Entry(width=31, font=entryFont)
hoverEventValue.grid(row=23, column=1, sticky='w,e')
hoverEventValue['state'] = 'disabled'

setEmpty(24, 0)

Spawn = tk.Button(font=entryFont, text='???????????????', height=2, command=Spawn)
Spawn.grid(row=25, column=1, sticky='we')

setEmpty(26, 0, sep_=False)


def askUpdate_thread2():
    global UPDATE, root,text_

    text_ = requests.get(
        verify=False, url='https://raw.githubusercontent.com/ANTmmmmm/ANTmmmmm.github.io/main/softwaresHighestVersion/RJT_editor.txt').text.replace(' ', '').replace('\n', '')

    try:
        with open('Temp/RJT_ver') as f:
            print(f.read())
            os.remove('Temp/RJT_ver')

    except FileNotFoundError:
        pass

    if VERSION != text_:
        update = messagebox.askyesno(title='????????????', message='???????????????????????????????????????')
        if update == True:
            if TYPE == 'EXE':
                with open('newVersion.exe', 'wb+') as f:
                    a = requests.get(verify=False, url=str(
                        'https://github.com/ANTmmmmm/RJT-editor/releases/download/v'+text_+'/RJT_editor_x64.exe')).content
                    f.write(a)
                    print('https://github.com/ANTmmmmm/RJT-editor/releases/download/v' +
                          text_+'/RJT_editor_x64.exe')
                try:
                    os.rename('RJT_editor_x64.exe', 'oldVersion.exe')
                except:
                    pass
                os.rename('newVersion.exe', 'RJT_editor_x64.exe')
                UPDATE = True
                root.destroy()
            else:
                with open('newVersion.zip', 'wb+') as f:
                    f.write(requests.get(verify=False, url=str(
                        'https://github.com/ANTmmmmm/RJT-editor/archive/refs/tags/v'+text_+'.zip')).content)
                print(
                    'https://github.com/ANTmmmmm/RJT-editor/archive/refs/tags/v'+text_+'.zip')
                with zipfile.ZipFile('.\\newVersion.zip') as f:
                    f.extractall('.\\')
                os.rename('RJT-editor-'+text_, 'newVersion')
                with open('newVersion/RJT_editor.py', encoding='UTF-8') as f:
                    with open('newVersion.py', 'w+', encoding='UTF-8') as f2:
                        f2.write(f.read())
                filelist = os.listdir('newVersion').copy()
                print(filelist)
                for i in filelist:
                    os.remove('newVersion/'+str(i))

                os.remove('newVersion.zip')
                os.removedirs('newVersion')
                os.rename('RJT_editor.py', 'oldVersion.py')
                os.rename('newVersion.py', 'RJT_editor.py')
                UPDATE = True
                root.destroy()


def goThread():
    th = threading.Thread(target=askUpdate_thread2)
    th.setDaemon(True)  # ????????????
    th.start()


goThread()
UPDATE = False
root.mainloop()

if TYPE!='EXE':
    if UPDATE == True:
        os.system('python RJT_editor.py')
else:
    if UPDATE==True:
        os.system('RJT_editor_x64.exe')
print(UPDATE)
