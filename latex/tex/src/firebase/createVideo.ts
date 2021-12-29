import * as functions from "firebase-functions";
import * as admin from "firebase-admin";

const firestore = admin.firestore();

exports.createVideo = functions.https.onCall(async (data, context) => {
    const email = context?.auth?.token.email;

    if (!email) {
        return {
            message: 'not authenticated'
        }
    }

    if (!data.title || !data.description || !data.link) {
        return {
            "success": false,
        };
    }

    const video = await firestore.collection("videos").add({
        "title": data.title,
        "description": data.description,
        "rawLink": data.link,
        "owner": email,
    });

    return {
        "success": video,
    };
});