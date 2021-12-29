import { getStorage, ref } from "firebase/storage";
import { v4 as uuidv4 } from 'uuid';

const fileName = uuidv4() + '_' + file.name;

const uploadTask = getStorage().ref(`${fileName}`).put(file);

uploadTask.on(
  "state_changed",
  (snapshot) => {
    const progress = Math.round(
      (snapshot.bytesTransferred / snapshot.totalBytes) * 100
    );
    setProgress(progress);
  },
  error => {
    console.log(error);
  },
  async () => {
    //After uploading the video
  }
);