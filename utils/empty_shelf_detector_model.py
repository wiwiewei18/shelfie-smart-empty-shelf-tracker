
class EmptyShelfDetectorModel:
    def __init__(self, model):
        self.model = model
        
    def detect(self, frame):
        results = self.model(frame)
        annotated_frame = results[0].plot()
        
        self.results = results
        
        return annotated_frame
    
    def get_detected_object_names(self):
        detected_object_names = []
    
        for result in self.results:
            for box in result.boxes:
                class_name = self.model.names[int(box.cls[0])]
                detected_object_names.append(class_name)
                
        return detected_object_names
    
    def count_detected_objects(self):
        return len(self.get_detected_object_names())