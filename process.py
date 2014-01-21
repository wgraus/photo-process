#!/usr/bin/env python
# encoding: utf-8
import shutil
import os
from os import listdir
from os.path import isfile, join
from gimpscript import GimpScript
from config import Config
from PIL import Image, ImageFile
from progressbar import ProgressBar

bar = ProgressBar('blue', width=30, block='█', empty=' ')


class ProcesBatch():
    ''' Procesa les fotos
    '''
    def __init__(self):
        ''' Carrega la configuracio
        '''
        self.c = Config()
        self.dir_treball = os.getcwd()

    def l(self, p):
        print "%s ..." % p

    def copiar(self, a, b):
        ''' Copia carpeta
        '''
        print "-> %s" % a
        print "<- %s" % b
        shutil.copytree(a, b)

    def llista_imatges(self):
        ''' Carrega les imatges
        '''
        self.l("Loading Images")
        fotos = self.c.dir_fotos
        llista = [f for f in listdir(fotos) if isfile(join(fotos, f))]
        return llista

    def barra(self, image, llista):
        ''' Barra de carrega
        '''
        i = llista.index(image) + 1
        p = float(i / float(len(llista)))
        percent = int(p * 100)
        bar.render(percent, '%d ▻ %s' % (i, image))

    def processar(self):
        ''' Procesa les imatges
        '''
        self.l("Processing")
        llista_im = self.llista_imatges()
        for image in llista_im:
            self.barra(image, llista_im)
            i = os.path.join(self.dir_treball, self.c.dir_fotos, image)
            gs = GimpScript(i)
            gs.run()
        print

    def carpeta_original(self):
        ''' Copia carpeta original
        '''
        print "Copying Original ..."
        a = os.path.join(self.dir_treball, self.c.dir_fotos)
        b = os.path.join(self.c.dir_fotografies, self.c.original)
        self.copiar(a, b)

    def carpeta_edit(self):
        ''' Copia carpeta edit
        '''
        print "Copying Edit ..."
        a = os.path.join(self.dir_treball, self.c.dir_fotos)
        b = os.path.join(self.c.dir_fotografies, self.c.edit)
        self.copiar(a, b)
        shutil.rmtree(a)

    def thumbs(self, i, image):
        ''' Generate thumbs
        '''
        ruta = os.path.join(self.c.dir_fotos, image)
        dw = self.c.dir_web
        tp = self.c.tipus
        ta = self.c.tag
        if not os.path.exists(os.path.join(dw, tp, ta)):
            os.makedirs(os.path.join(dw, tp, ta))
        ImageFile.MAXBLOCK = 2**20

        # sizes
        size_thumb = (self.c.thumb_whith, self.c.thumb_height)
        size_orig = (self.c.orig_whith, self.c.orig_height)

        # names
        original_pattern = '%s%s_%s.jpg' % (self.c.pattern, str(i),
                           self.c.thumb_pattern)
        thumb_pattern = '%s%s.jpg' % (self.c.pattern, str(i))

        # paths
        f = os.path.join(dw, tp, ta, original_pattern)
        t = os.path.join(dw, tp, ta, thumb_pattern)

        # resizes
        original = Image.open(ruta)
        _ = original.resize(size_thumb, Image.ANTIALIAS)
        _.save(f, optimize=True, quality=self.c.quality, progressive=True)
        _ = original.resize(size_orig, Image.ANTIALIAS)
        _.save(t, optimize=True, quality=self.c.quality, progressive=True)

    def carpeta_web(self):
        ''' Procesa les imatges
        '''
        self.l("Processing")
        l = self.llista_imatges()
        for i, image in enumerate(l):
            self.barra(image, l)
            self.thumbs(i, image)
        print

    def run(self):
        ''' Executa el proces
        '''
        self.carpeta_original()
        self.processar()
        self.carpeta_web()
        self.carpeta_edit()
