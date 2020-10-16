# Analyze Text with a TextAnalyzer object!
#
# By:

import unittest  # import the library needed for testing
import math
import csv
import os


class TextAnalyzer:

    def __init__(self, filepath):
        """Initializes the TextAnalyzer object, using the file at filepath.
        Initialize the following instance variables: filepath (string),
        lines (list)"""

    def sentence_count(self):
        """Returns the number of sentences in the file (seperated by .)
        Note that if there are no '.' in the sentences return 1"""

    def words(self):
        """Returns a list of words without punctuations and all lower case.
        For example : 'Cat!' should be 'cat'."""
        # Uncomment the next line

        #punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    def word_count(self):
        """Returns the number of words in the file. A word is defined as any
        text that is separated by whitespace (spaces, newlines, or tabs)."""

    def vocabulary(self):
        """Returns a list of the unique words in the text, sorted in
        alphabetical order. Capitalization and punctiuation should be ignored, so 'Cat!' is the
        same word as 'cat'. The returned words should be all lower-case."""

    def frequencies(self):
        """Returns a dictionary of the words in the text and the count of how
        many times they appear. The words are the keys, and the counts are the
        values. All the words should be lower case and without punctuations. The order of the keys
        doesn't matter."""

    def frequency_of(self, word):
        """Returns the number of times word appears in the text. Capitalization and punctuation
        should be ignored, so 'Cat!' is the same word as 'cat'. If the word does not exist in the text,
        then return 0"""

    def percent_frequencies(self):
        """Returns a dictionary of the words in the text and the frequency of the
        words as a percentage of the text. The words are the keys, and the
        counts are the values. All the words should be lower case and without punctuations. The order
        of the keys doesn't matter."""

    def most_common(self):
        """Returns the most common word in the text and its frequency in a list.
            There might be a case where multiple words have the same frequency,
            in that case return one of the most common words """
        # Example ouput : ['so', 6]

    def read_sample_csv(self):
        """Reads the sample.csv file and returns the list of fieldnames"""

    def write_analysis_details(self, csvfile):
        """Writes the details of the textual analysis to the csvfile.
        Refer to sample.csv for an example of how this should look.
        Note that for most common word, just write the word and not its frequency"""

        #filepath, unique words, total words, line count, most common word

    def similarity_with(self, other_text_analyzer):
        """Extra credit. Calculates the similarity between this text and
        the other text using cosine similarity."""

# These are the tests.

class TestSentenceCount(unittest.TestCase):

    def test_sentence_count_tiny1(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        self.assertEqual(ta.sentence_count(), 1)
        self.assertEqual(ta.sentence_count(), 1) # Check that it works when called a second time

    def test_line_count_tiny3(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_3.txt")
        self.assertEqual(ta.sentence_count(), 3)
        self.assertEqual(ta.sentence_count(), 3) # Check that it works when called a second time

    def test_line_count_the_buckeye_battle_cry(self):
        ta = TextAnalyzer("files_for_testing/buckeye_battle_cry.txt")
        self.assertEqual(ta.sentence_count(), 3)
        self.assertEqual(ta.sentence_count(), 3) # Check that it works when called a second time

class TestWords(unittest.TestCase):

    def test_words_tiny1(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        self.assertEqual(ta.words(), ['coffee', 'is', 'so', 'good'])

    def test_words_tiny2(self):
        ta2 = TextAnalyzer("files_for_testing/tinyfile_2.txt")
        self.assertEqual(ta2.words(), ['you', 'hate', 'tea'])

    def test_words_tiny3(self):
        ta3 = TextAnalyzer("files_for_testing/tinyfile_4.txt")
        self.assertEqual(ta3.words(), ['i', 'love', 'coffee', 'so', 'so', 'so', 'so', 'so', 'so', 'much'])

class TestWordCount(unittest.TestCase):

    def test_word_count_tiny1(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        self.assertEqual(ta.word_count(), 4)
        self.assertEqual(ta.word_count(), 4) # Check that it works when called a second time

    def test_word_count_tiny3(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_3.txt")
        self.assertEqual(ta.word_count(), 24)
        self.assertEqual(ta.word_count(), 24) # Check that it works when called a second time

    def test_word_count_the_osusong(self):
        ta = TextAnalyzer("files_for_testing/osusong.txt")
        self.assertEqual(ta.word_count(), 7)
        self.assertEqual(ta.word_count(), 7) # Check that it works when called a second time

class TestFrequencies(unittest.TestCase):

    def test_frequencies_tiny1(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        self.assertEqual(ta.frequencies()['coffee'], 1)
        self.assertEqual(ta.frequencies()['is'], 1)
        self.assertEqual(ta.frequencies()['good'], 1)

    def test_frequencies_tiny2(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_2.txt")
        self.assertEqual(ta.frequencies()['you'], 1)
        self.assertEqual(ta.frequencies()['hate'], 1)
        self.assertEqual(ta.frequencies()['tea'], 1)

    def test_frequencies_tiny4(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_4.txt")
        self.assertEqual(ta.frequencies()['i'], 1)
        self.assertEqual(ta.frequencies()['love'], 1)
        self.assertEqual(ta.frequencies()['coffee'], 1)
        self.assertEqual(ta.frequencies()['so'], 6)
        self.assertEqual(ta.frequencies()['much'], 1)

class TestFrequencyOf(unittest.TestCase):

    def test_frequency_of_tiny1(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        self.assertEqual(ta.frequency_of('coffee'), 1)
        self.assertEqual(ta.frequency_of('is'), 1)
        self.assertEqual(ta.frequency_of('so'), 1)
        self.assertEqual(ta.frequency_of('good'), 1)

    def test_frequency_of_osusong(self):
        ta = TextAnalyzer("files_for_testing/osusong.txt")
        self.assertEqual(ta.frequency_of('come'), 1)
        self.assertEqual(ta.frequency_of('on'), 1)
        self.assertEqual(ta.frequency_of('ohio'), 1)
        self.assertEqual(ta.frequency_of('victory'), 1)
        self.assertEqual(ta.frequency_of('through'), 1)

    def test_frequency_of_tiny2(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_2.txt")
        self.assertEqual(ta.frequency_of('you'), 1)
        self.assertEqual(ta.frequency_of('hate'), 1)
        self.assertEqual(ta.frequency_of('tea'), 1)
        self.assertEqual(ta.frequency_of('coffee'), 0)


class TestVocabulary(unittest.TestCase):

    def test_vocabulary_tiny1(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        self.assertEqual(ta.vocabulary(), ['coffee', 'good', 'is', 'so'])

    def test_vocabulary_tiny3(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_3.txt")
        self.assertEqual(ta.vocabulary(), ['coffee', 'hate', 'i', 'juice', 'love', 'much', 'so', 'tea'])

    def test_vocabulary_tiny4(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_4.txt")
        self.assertEqual(ta.vocabulary(), ['coffee', 'i', 'love', 'much', 'so'])

class TestPercentFrequencyOf(unittest.TestCase):

    def test_percent_frequency_of_tiny1(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        self.assertIn('coffee', ta.percent_frequencies())
        self.assertIn('is', ta.percent_frequencies())
        self.assertIn('good', ta.percent_frequencies())
        self.assertAlmostEqual(ta.percent_frequencies()['is'], 1/4)
        self.assertAlmostEqual(ta.percent_frequencies()['good'], 1/4)
        self.assertAlmostEqual(ta.percent_frequencies()['coffee'], 1/4)

    def test_percent_frequency_of_tiny3(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_3.txt")
        self.assertIn('i', ta.percent_frequencies())
        self.assertIn('love', ta.percent_frequencies())
        self.assertIn('coffee', ta.percent_frequencies())
        self.assertIn('so', ta.percent_frequencies())
        self.assertIn('much', ta.percent_frequencies())
        self.assertIn('hate', ta.percent_frequencies())
        self.assertIn('juice', ta.percent_frequencies())
        self.assertAlmostEqual(ta.percent_frequencies()['i'], 3/24)
        self.assertAlmostEqual(ta.percent_frequencies()['love'], 2/24)
        self.assertAlmostEqual(ta.percent_frequencies()['coffee'], 1/24)
        self.assertAlmostEqual(ta.percent_frequencies()['tea'], 1/24)
        self.assertAlmostEqual(ta.percent_frequencies()['juice'], 1/24)
        self.assertAlmostEqual(ta.percent_frequencies()['much'], 3/24)
        self.assertAlmostEqual(ta.percent_frequencies()['so'], 12/24)
        self.assertAlmostEqual(ta.percent_frequencies()['hate'], 1/24)

    def test_percent_frequency_of_tiny4(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_4.txt")
        self.assertAlmostEqual(ta.percent_frequencies()['i'], 1/10)
        self.assertAlmostEqual(ta.percent_frequencies()['love'], 1/10)
        self.assertAlmostEqual(ta.percent_frequencies()['coffee'], 1/10)
        self.assertAlmostEqual(ta.percent_frequencies()['so'], 6/10)
        self.assertAlmostEqual(ta.percent_frequencies()['much'], 1/10)

class TestMostCommon1(unittest.TestCase):

    def test_most_common_1_tiny3(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_3.txt")
        self.assertEqual(ta.most_common()[0], 'so')

    def test_most_common_1_tiny4(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_4.txt")
        self.assertEqual(ta.most_common()[0], 'so')

class TestMostCommonMultipleClearCases(unittest.TestCase):

    def test_most_common_multiple_tiny1(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        self.assertEqual(ta.most_common()[1], 1)

class TestReadSampleCSV(unittest.TestCase):

    def test_reading_sample_csv(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_4.txt")
        self.assertEqual(ta.read_sample_csv(), ['filepath', 'total words', 'line count', 'most common word'])

class TestWriteAnalysis(unittest.TestCase):

    def test_write_analysis_details(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_4.txt")
        ta.write_analysis_details('test.csv')
        f = open('test.csv')
        csv_reader = csv.reader(f, delimiter=',')
        lines = [r for r in csv_reader]
        self.assertEqual(lines[0], ['filepath', 'total words', 'line count', 'most common word'])
        self.assertEqual(lines[1], ['files_for_testing/tinyfile_4.txt', '10','1','so'])
        f.close()


class TestSimilarity(unittest.TestCase):
    def test_similarity_when_all_same(self):
        ta1 = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        ta2 = TextAnalyzer("files_for_testing/tinyfile_2.txt")
        self.assertAlmostEqual(ta1.similarity_with(ta2), 0.0)

    def test_similarity_when_all_different(self):
        ta1 = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        ta2 = TextAnalyzer("files_for_testing/tinyfile_3.txt")
        self.assertAlmostEqual(ta1.similarity_with(ta2), 1.0833333333333333)

    def test_similarity_when_somewhat_different(self):
        ta1 = TextAnalyzer("files_for_testing/tinyfile_2.txt")
        ta2 = TextAnalyzer("files_for_testing/tinyfile_3.txt")
        self.assertAlmostEqual(ta1.similarity_with(ta2), 0.16666666666666666)


    def test_similarity_when_somewhat_different2(self):
        ta1 = TextAnalyzer("files_for_testing/tinyfile_4.txt")
        ta2 = TextAnalyzer("files_for_testing/tinyfile_3.txt")
        self.assertAlmostEqual(ta1.similarity_with(ta2), 1.125)


if __name__ == "__main__":
    # Un-comment this line when you are ready to run the unit tests.
    unittest.main(verbosity=2)

    # You can uncomment out some of these lines to do some simple tests with print statements.
    # Or, use your own print statements here as well!
    fightsong = TextAnalyzer("files_for_testing/fightsong.txt")
    osusong = TextAnalyzer("files_for_testing/osusong.txt")
    print("Sentence count is ", fightsong.sentence_count())
    print("Words list is ", fightsong.words())
    print("Word count is ", fightsong.word_count())
    print("Vocabulary is ", fightsong.vocabulary())
    print("Frequencies are ", fightsong.frequencies())
    print("Most common word and its frequence is ", fightsong.most_common())
    print("Percent frequencies are ", fightsong.percent_frequencies())

    ta1 = TextAnalyzer("files_for_testing/tinyfile_1.txt")
    ta2 = TextAnalyzer("files_for_testing/tinyfile_1.txt")
    print(fightsong.similarity_with(osusong))

    ta1 = TextAnalyzer("files_for_testing/tinyfile_1.txt")
    ta2 = TextAnalyzer("files_for_testing/tinyfile_2.txt")
    print(ta1.similarity_with(ta2))
