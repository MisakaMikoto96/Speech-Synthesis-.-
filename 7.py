import codecs

from six import string_types

from nltk import compat
from nltk.util import Index

from nltk.corpus.reader.util import *
from nltk.corpus.reader.api import *

class CMUDictCorpusReader(CorpusReader):

  def entries(self):
        """
        :return: the cmudict lexicon as a list of entries
        containing (word, transcriptions) tuples.
        """
        return concat([StreamBackedCorpusView(fileid, read_cmudict_block,
                                              encoding=enc)
                       for fileid, enc in self.abspaths(None, True)])


  def raw(self):
        """
        :return: the cmudict lexicon as a raw string.
        """
        fileids = self._fileids
        if isinstance(fileids, string_types):
            fileids = [fileids]
        return concat([self.open(f).read() for f in fileids])


  def words(self):
        """
        :return: a list of all words defined in the cmudict lexicon.
        """
        return [word.lower() for (word, _) in self.entries()]


  def dict(self):
        """
        :return: the cmudict lexicon as a dictionary, whose keys are
        lowercase words and whose values are lists of pronunciations.
        """
        return dict(Index(self.entries()))


  def read_cmudict_block(stream):
    entries = []
    while len(entries) < 100: # Read 100 at a time.
        line = stream.readline()
        if line == '': return entries # end of file.
        pieces = line.split()
        entries.append( (pieces[0].lower(), pieces[2:]) )
    return entries
