from google_trans_new_that_works import google_translator

detector = google_translator()
detect_result = detector.detect('สวัสดีจีน')
# <Detect text=สวัสดีจีน >
print(detect_result)
