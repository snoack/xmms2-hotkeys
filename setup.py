from distutils.core import setup

setup(name='xmms2-notify',
      version='0.1',
      description='Client for XMMS2 that translates HAL "media key" events to playback commands.',
      author='Sebastian Noack',
      author_email='sebastian.noack@gmail.com',
      classifiers=[
          'Environment :: X11',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: Gnu Public License V3.0',
          'Operating System :: POSIX',
          'Programming Language :: Python',
      ],
      scripts=['xmms2-hotkeys'])
