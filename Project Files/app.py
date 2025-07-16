from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model('vgg16_butterfly_model.h5')

class_labels = [
    "ADONIS", "AFRICAN GIANT SWALLOWTAIL", "AMERICAN SNOOT", "AN 88", "APPOLLO", "ATALA",
    "BANDED ORANGE HELICONIAN", "BANDED PEACOCK", "BECKERS WHITE", "BLACK HAIRSTREAK",
    "BLUE MORPHO", "BLUE SPOTTED CROW", "BROWN SIPROETA", "CABBAGE WHITE", "CAIRNS BIRDWING",
    "CHECQUERED SKIPPER", "CHESTNUT", "CLEOPATRA", "CLODIUS PARNASSIAN", "CLOUDED SULPHUR",
    "COMMON BANDED AWL", "COMMON WOOD-NYMPH", "COPPER TAIL", "CRECENT", "CRIMSON PATCH",
    "DANAID EGGFLY", "EASTERN COMA", "EASTERN DAPPLE WHITE", "EASTERN PINE ELFIN", "ELBOWED PIERROT",
    "GOLD BANDED", "GREAT EGGFLY", "GREAT JAY", "GREEN CELLED CATTLEHEART", "GREY HAIRSTREAK",
    "INDRA SWALLOW", "IPHICLUS SISTER", "JULIA", "LARGE MARBLE", "MALACHITE", "MANGROVE SKIPPER",
    "MESTRA", "METALMARK", "MILBERTS TORTOISESHELL", "MONARCH", "MOURNING CLOAK", "ORANGE OAKLEAF",
    "ORANGE TIP", "ORCHARD SWALLOW", "PAINTED LADY", "PAPER KITE", "PEACOCK", "PINE WHITE",
    "PIPEVINE SWALLOW", "POPINJAY", "PURPLE HAIRSTREAK", "PURPLISH COPPER", "QUESTION MARK",
    "RED ADMIRAL", "RED CRACKER", "RED POSTMAN", "RED SPOTTED PURPLE", "SCARCE SWALLOW",
    "SILVER SPOT SKIPPER", "SLEEPY ORANGE", "SOOTYWING", "SOUTHERN DOGFACE", "STRAITED QUEEN",
    "TROPICAL LEAFWING", "TWO BARRED FLASHER", "ULYSES", "VICEROY", "WOOD SATYR",
    "YELLOW SWALLOW TAIL", "ZEBRA LONG WING"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        img_path = os.path.join('static', 'upload.jpg')
        file.save(img_path)

        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        predictions = model.predict(img_array)
        predicted_index = np.argmax(predictions[0])
        predicted_label = class_labels[predicted_index]
        confidence = round(float(np.max(predictions[0])) * 100, 2)

        return render_template('output.html',
                               prediction=predicted_label,
                               confidence=confidence,
                               image_file=img_path)
    return "Error", 500

if __name__ == '__main__':
    app.run(debug=True)
