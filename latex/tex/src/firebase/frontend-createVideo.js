import { getFunctions, httpsCallable } from "firebase/functions";

const functions = getFunctions();
const createVideo = httpsCallable(functions, 'createVideo');

const result = await createVideo({
  title: title,
  description: description,
  link: fileName
});