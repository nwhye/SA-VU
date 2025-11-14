import numpy as np
import cv2
import torch
import os
import json
from torchvision.transforms.functional import normalize, resize
from torchvision.models import resnet18, convnext_base, inception_v3

with open('imagenet_class_index.json') as labels_file:
    labels = json.load(labels_file)

models = [resnet18(pretrained=True).eval(), convnext_base(pretrained=True), inception_v3(pretrained=True).eval()]
namings = ["ResNet18 model: ", "ConvNeXt model:", "Inception model:"]

for i, model in enumerate(models):

    true_results = 0
    all_results = 0
    print(namings[i])

    for source_f in os.scandir('./albatross/'):

        file = source_f.path
        image = cv2.imread(file)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img = torch.from_numpy(image)
        img = img.permute(2, 0, 1)
        print('Image shape:', img.shape)
        input_tensor = normalize(resize(img, [224, 224]) / 255., [0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        out = model(input_tensor.unsqueeze(0))
        out = out.detach().cpu().numpy()
        idx = np.argmax(out, axis=1)
        str_idx = str(idx[0])
        print(labels[str_idx])

        if labels[str_idx][1] == "albatross":
            true_results += 1
        all_results += 1

    accuracy = round(true_results/all_results*100)
    print('Accuracy: ' + str(accuracy) + '%\n')