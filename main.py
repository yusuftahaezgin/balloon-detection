import cv2
from ultralytics import YOLO

# colab de egittigim modeli yukledim
model = YOLO('best.pt')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()


# red balloon id si bulma
class_names = model.names
try:
    RED_BALLOON_ID = [k for k, v in class_names.items() if v == 'red balloon'][0]
    print(f"Kirmizi Balon sinif ID'si bulundu: {RED_BALLOON_ID}")
except IndexError:
    print("Modelde 'red balloon' sınıfı bulunamadı. Lütfen data.yaml dosyasını kontrol edin.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape
    screen_center_x = width // 2
    screen_center_y = height // 2

    # model ekranı tarıyor
    results = model(frame, verbose=False) #verbose=False terminale surekli olarak bilgi basilmasini engeller

    for result in results:
        for box in result.boxes:
            # sadece kırmızı balonları isle
            if int(box.cls) == RED_BALLOON_ID:
                x1, y1, x2, y2 = map(int, box.xyxy[0]) # balon etrafındaki sınırlayıcı kutunun koordinatlarını
                # sol-ust kose (x1, y1), sag-alt kose (x2, y2)

                balloon_center_x = (x1 + x2) // 2
                balloon_center_y = (y1 + y2) // 2

                # erkanın merkezi sol ust kosededir bu ayarlar oan gore
                konum_y = "yukari" if balloon_center_y < screen_center_y else "asagi"
                konum_x = "sol" if balloon_center_x < screen_center_x else "sag"
                konum_mesaji = f"Kirmizi Balon: {konum_y}-{konum_x}"

                # balonun etrafına kırmızı renkte bir dikdortgen cizer
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                # konum bilgisini yaz
                cv2.putText(frame, konum_mesaji, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # referans icin ekranın ortasına mavi nokta cizdik
    cv2.circle(frame, (screen_center_x, screen_center_y), 5, (255, 0, 0), -1)

    cv2.imshow('Kirmizi Balon Tespiti', frame)

    # 'q' tuşuna basinca programdan cık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()