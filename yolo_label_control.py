import cv2
import os
import argparse
from pathlib import Path


def view_images_with_labels(images_dir, labels_dir, class_name_dir):
    
    class_names = Path(class_name_dir).read_text().strip().split('\n')

    img_list = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    index = 0
    
    while True:
        if index >= len(img_list):
            print("Verisetindeki son goruntu")
            break
            
        img_path = os.path.join(images_dir, img_list[index])
        img = cv2.imread(img_path)
        
        if img is None:
            print(f"Image dosyasi okunmadi: {img_path}")
            index += 1
            continue
        
        height, width = img.shape[:2]
        
        label_name = os.path.splitext(img_list[index])[0] + '.txt'
        label_path = os.path.join(labels_dir, label_name)
        
        if os.path.exists(label_path):
            try:
                with open(label_path, 'r') as f:
                    for line in f.readlines():
                        class_id, xc, yc, w, h = map(float, line.strip().split())

                        xcenter = int(width * xc)
                        ycenter = int(height * yc)
                        rwidth = int(width * w)
                        rheight = int(height * h)

                        x1 = xcenter - (rwidth // 2)
                        y1 = ycenter - (rheight // 2)
                        x2 = xcenter + (rwidth // 2)
                        y2 = ycenter + (rheight // 2)

                        class_label = class_names[int(class_id)] if int(class_id) < len(class_names) else f"Class {int(class_id)}"

                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(img, class_label, 
                                    (x1, y1 - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (0, 255, 0), 2)
                
                print(f"Image: {img_list[index]}")
                print(f"Label: {label_name}")
                
            except Exception as e:
                print(f"Label dosyasi okunmadi: {e}")
        else:
            print(f"Label dosyasi bulunamadi: {label_path}")
        
        cv2.imshow("frame", img)
        
        key = cv2.waitKey(0)
        
        if key == ord('a'):  
            index += 1
        elif key == ord('q'):  
            break
    
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLO Etiket Goruntuleme Kodu")

    parser.add_argument("--images", "-i", required=True, help="Images klasorunun bulundugu dizin")
    parser.add_argument("--labels", "-l", required=True, help="Labels klasorunun bulunduğu dizin")
    parser.add_argument("--classes", "-c", required=True, help="Etiketi isimlerinin bulundugu dosyanin dizini")

    args = parser.parse_args()

    view_images_with_labels(args.images, args.labels, args.classes)
