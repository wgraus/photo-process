import subprocess as sbp


class GimpScript():
    '''GimpScript'''
    def __init__(self, image):
        ''' Load Gimp batch command
        '''
        r = "\"%s\"" % image
        g = 'gimp'
        i = '-i'
        b = '-b'
        s = 'elsamuko-lomo-batch'
        p = '1.5 10 10 0.8 0 0 0 0 0 FALSE FALSE TRUE FALSE 0 0 115'
        q = 'gimp-quit 0'
        self.cmd = "%s %s %s '(%s %s %s)' %s '(%s)' 2> /dev/null" \
                   % (g, i, b, s, r, p, b, q)

    def run(self):
        ''' Run gimp process
        '''
        g = sbp.Popen(self.cmd, stdin=sbp.PIPE, stdout=sbp.PIPE,
                      stderr=sbp.PIPE, shell=True)
        g.stdout.read()
