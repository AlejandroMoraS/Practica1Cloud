import keyvalue.sqlitekeyvalue as KeyValue
import keyvalue.parsetriples as ParseTriple
import keyvalue.stemmer as Stemmer


# Make connections to KeyValue
kv_labels = KeyValue.SqliteKeyValue("sqlite_labels.db","labels",sortKey=True)
kv_images = KeyValue.SqliteKeyValue("sqlite_images.db","images")

# Process Logic.
labelDataset = ParseTriple.ParseTriples('./datasets/labels_en.ttl')
imageDataset = ParseTriple.ParseTriples('./datasets/images_en.ttl')

#print(labelDataset.getNext())
print(imageDataset.getNextImages())
print(imageDataset.getNextImages())
print(imageDataset.getNextImages())
print(imageDataset.getNextImages())
print(imageDataset.getNextImages())
print(imageDataset.getNextImages())
print(imageDataset.getNextImages())
print(imageDataset.getNextImages())
print(imageDataset.getNextImages())
print(imageDataset.getNextImages())
print(imageDataset.getNextImages())
print(imageDataset.getNextImages())
print(imageDataset.getNextImages())






#kv_images = KeyValue.SqliteKeyValue('./datasets/labels_en.ttl' , "images")

#putsort pa lables
#put pa imagenes
#kv_labels.putSort('test2', '2', 'pollo')

'''for x in range(1000):
    kv_labels.putSort(labelDataset.getNext()[0], labelDataset.getNext()[1], labelDataset.getNext()[2])
    print(labelDataset.getNext()) '''

'''for x in range(1000):
    kv_images.put(imageDataset.getNextImages()[0], imageDataset.getNextImages()[2])
    print(imageDataset.getNextImages())'''


print(kv_labels.get('http://dbpedia.org/resource/AfghanistanCommunications'))
print(kv_labels.get('test2'))

# Close KeyValues Storages
kv_labels.close()
kv_images.close()







