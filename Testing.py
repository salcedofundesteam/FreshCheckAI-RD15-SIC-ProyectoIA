import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

model = load_model("clasificador_frutas.h5")

img_path = "Banana-Single.jpg"

img = image.load_img(img_path, target_size=(150,150))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

pred = model.predict(img_array)

'''
clases = [
    "freshapples",
    "freshbanana",
    "freshoranges",
    "rottenapples",
    "rottenbanana",
    "rottenoranges",
    "unripe apple",
    "unripe banana",
    "unripe orange"
]
'''

clases = [
    "Manzana fresca",
    "Banana fresca",
    "Naranja fresca",
    "Manzana podrida",
    "Banana podrida",
    "Naranja podrida",
    "Manzana verde",
    "Banana verde",
    "Naranja verde"
]


resultado = clases[np.argmax(pred)]
print("predicción:", resultado)

'''
Found 16217 images belonging to 9 classes.
Found 3739 images belonging to 9 classes.

Epoch 1/10
507/507 ━━━━━━━━━━━━━━━━━━━━ 112s 218ms/step - accuracy: 0.6592 - loss: 0.8410 - val_accuracy: 0.7879 - val_loss: 0.5272
Epoch 2/10
507/507 ━━━━━━━━━━━━━━━━━━━━ 113s 222ms/step - accuracy: 0.8035 - loss: 0.4693 - val_accuracy: 0.8320 - val_loss: 0.4281
Epoch 3/10
507/507 ━━━━━━━━━━━━━━━━━━━━ 119s 234ms/step - accuracy: 0.8489 - loss: 0.3625 - val_accuracy: 0.8673 - val_loss: 0.3377
Epoch 4/10
507/507 ━━━━━━━━━━━━━━━━━━━━ 121s 239ms/step - accuracy: 0.8901 - loss: 0.2760 - val_accuracy: 0.8700 - val_loss: 0.3219
Epoch 5/10
507/507 ━━━━━━━━━━━━━━━━━━━━ 112s 220ms/step - accuracy: 0.9233 - loss: 0.1985 - val_accuracy: 0.8821 - val_loss: 0.3118
Epoch 6/10
507/507 ━━━━━━━━━━━━━━━━━━━━ 111s 219ms/step - accuracy: 0.9457 - loss: 0.1462 - val_accuracy: 0.8941 - val_loss: 0.3211
Epoch 7/10
507/507 ━━━━━━━━━━━━━━━━━━━━ 105s 207ms/step - accuracy: 0.9647 - loss: 0.0989 - val_accuracy: 0.8893 - val_loss: 0.3368
Epoch 8/10
507/507 ━━━━━━━━━━━━━━━━━━━━ 108s 214ms/step - accuracy: 0.9798 - loss: 0.0629 - val_accuracy: 0.8919 - val_loss: 0.4220
Epoch 9/10
507/507 ━━━━━━━━━━━━━━━━━━━━ 113s 223ms/step - accuracy: 0.9785 - loss: 0.0651 - val_accuracy: 0.8821 - val_loss: 0.4532
Epoch 10/10
507/507 ━━━━━━━━━━━━━━━━━━━━ 108s 213ms/step - accuracy: 0.9834 - loss: 0.0526 - val_accuracy: 0.8922 - val_loss: 0.4768'''