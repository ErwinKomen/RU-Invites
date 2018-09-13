import os
import cherrypy

CONFIGURATION = {
        "/": {
                'tools.sessions.on': True, 
                'tools.staticdir.root': os.path.abspath(os.getcwd()),
             },
        "/static": {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': './static'
             },
        }

SERVE_PORT = 6001   # 443    # 6001

KEIZER_BASE = "static/img"

KEIZERS = [
    {"id": 1, "doel": "kind", "geslacht": "m", "naam": "Caligula",       "file": "13192017765_a078c7b2f5_o.jpg"},
    {"id": 2, "doel": "kind", "geslacht": "m", "naam": "Caligula",       "file": "13192024785_46eae3c17e_o.jpg"},
    {"id": 3, "doel": "kind", "geslacht": "m", "naam": "Marcus Aurelius", "file": "5398415839_f3af34929c_o.jpg"},
    {"id": 4, "doel": "kind", "geslacht": "m", "naam": "Marcus Aurelius", "file": "10540130345_04d4159a68_o.jpg"},
    {"id": 5, "doel": "kind", "geslacht": "v", "naam": "Crispina",       "file": "12453754554_34a994a30a_o.jpg"},
    {"id": 6, "doel": "kind", "geslacht": "v", "naam": "Crispina",       "file": "19014212733_69fd24d5e2_o.jpg"},
    {"id": 7, "doel": "volwassene", "geslacht": "m", "naam": "Augustus",       "file": "14647638801_c194ae825d_o.jpg"},
    {"id": 8, "doel": "volwassene", "geslacht": "m", "naam": "Augustus",       "file": "26578107461_76aa89b9da_o.jpg"},
    {"id": 9, "doel": "volwassene", "geslacht": "m", "naam": "Caracalla", "file": "13647480653_e371dc7e58_o - Copy.jpg"},
    {"id": 10, "doel": "volwassene", "geslacht": "m", "naam": "Caracalla", "file": "31781295674_330b4e7cb1_o.jpg"},
    {"id": 11, "doel": "volwassene", "geslacht": "m", "naam": "Constantijn", "file": "20180304_125203604_iOS.jpg"},
    {"id": 12, "doel": "volwassene", "geslacht": "m", "naam": "Constantijn", "file": "20180304_131936179_iOS.jpg"},
    {"id": 13, "doel": "volwassene", "geslacht": "m", "naam": "Hadrianus", "file": "14601312834_83cff6550e_o.jpg"},
    {"id": 14, "doel": "volwassene", "geslacht": "m", "naam": "Hadrianus", "file": "20410706734_4101a614cc_o.jpg"},
    {"id": 15, "doel": "volwassene", "geslacht": "m", "naam": "Hadrianus", "file": "8115667122_32efffa1d4_o.jpg"},
    {"id": 16, "doel": "volwassene", "geslacht": "m", "naam": "Nero", "file": "8994119108_dc8ff055e0_o.jpg"},
    {"id": 17, "doel": "volwassene", "geslacht": "m", "naam": "Septimius Severus", "file": "13543792233_362dc3cbac_o.jpg"},
    {"id": 18, "doel": "volwassene", "geslacht": "m", "naam": "Septimius Severus", "file": "13648215765_6f32ea4d1d_o.jpg"},
    {"id": 19, "doel": "volwassene", "geslacht": "m", "naam": "Vespasianus", "file": "13646730625_5be8085714_o.jpg"},
    {"id": 20, "doel": "volwassene", "geslacht": "v", "naam": "Agrippina Minor", "file": "12949521044_ed56e66240_o.jpg"},
    {"id": 21, "doel": "volwassene", "geslacht": "v", "naam": "Antonia Minor", "file": "12990755044_a1986e33af_o.jpg"},
    {"id": 22, "doel": "volwassene", "geslacht": "v", "naam": "Antonia Minor", "file": "24366567479_5e418dd5b4_o.jpg"},
    {"id": 23, "doel": "volwassene", "geslacht": "v", "naam": "Faustina Minor", "file": "10540109095_569302c212_o.jpg"},
    {"id": 24, "doel": "volwassene", "geslacht": "v", "naam": "Faustina Minor", "file": "12453403933_506b75b9fb_o.jpg"},
    {"id": 25, "doel": "volwassene", "geslacht": "v", "naam": "Faustina Minor", "file": "13912229199_db39ef2c21_o.jpg"},
    {"id": 26, "doel": "volwassene", "geslacht": "v", "naam": "Julia Domna", "file": "12967363173_d7ee175bde_o.jpg"},
    {"id": 27, "doel": "volwassene", "geslacht": "v", "naam": "Julia Domna", "file": "12967516504_2957644b42_o.jpg"},
    {"id": 28, "doel": "volwassene", "geslacht": "v", "naam": "Livia", "file": "12949093165_46b0a2e7ef_o.jpg"},
    {"id": 29, "doel": "volwassene", "geslacht": "v", "naam": "Livia", "file": "21784811235_47e3cd0a95_o.jpg"},
    {"id": 30, "doel": "volwassene", "geslacht": "v", "naam": "Vibia Sabina", "file": "12972132095_ff4aeb7533_o.jpg"},
    {"id": 31, "doel": "volwassene", "geslacht": "v", "naam": "Vibia Sabina", "file": "12453693294_9a70e3ac15_o.jpg"},
#    {"id": 32, "doel": "kind", "geslacht": "v", "naam": "Sallustia Orbiana", "file": "25454131770_9a838cbcb3_o.jpg"},

    ]