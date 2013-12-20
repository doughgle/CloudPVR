'''
Created on Feb 25, 2013

@author: dough
'''
import unittest
from recording import Recording, RecordingDestinationError
import os

class TestRecording(unittest.TestCase):

    def setUp(self):
        self.rec = Recording()
        
    def test_hasName(self):
        self.assertIsInstance(self.rec.name, str)
        
    def test_canEditNameAfterCreation(self):
        new_name = "my 1st recording"
        self.rec.name = new_name
        self.assertEqual(self.rec.name, new_name)
        
    def test_hasDestinationAddress(self):
        self.assertIsInstance(self.rec.destination, str)        
        
    def test_hasFilename(self):
        self.assertIsInstance(self.rec.filename, str)
        
    def test_hasDirectoryPath(self):
        self.assertIsInstance(self.rec.destination_dir, str)
        
    def test_destinationAddressIsValidForCreation(self):
        test_file = open(self.rec.destination, 'w')
        test_file.close()
        os.remove(test_file.name)
        
    def test_filenameForEachRecordingIsUnique_evenAfterGarbageCollection(self):
        filename_history = []
        self._create_batch_of_recordings_and_check_their_filenames_are_unique(filename_history)
        self._create_batch_of_recordings_and_check_their_filenames_are_unique(filename_history)
        
    def test_canSpecifyDestinationDirectoryOnCreation(self):        
        example_dest = os.getcwd()
        self.rec = Recording(destination_dir=example_dest)
        self.assertEqual(self.rec.destination_dir, example_dest)
        
    def test_destinationDirectoryDefaultsToDefaultDestinationDirectory(self):
        self.assertEqual(self.rec.destination_dir, Recording.DEFAULT_DESTINATION_DIR)
        
    def test_nonExistingDestinationIsRecordingDestinationError(self):
        self.assertRaises(RecordingDestinationError, Recording, destination_dir="/home/unlikely_directory_name_99")

    def _create_batch_of_recordings_and_check_their_filenames_are_unique(self, rec_filenames):
        for i in range(5):
            rec = Recording()
            rec_filenames.append(rec.filename)

        self.assertEqual(len(rec_filenames), len(set(rec_filenames)))

        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()