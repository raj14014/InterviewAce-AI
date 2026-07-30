import api from "./api";

export const getQuestion = async () => {
  const response = await api.get("/analysis/question");
  return response.data;
};

export const submitAnswer = async (
  question: string,
  duration: number,
  audio: File
) => {
  const formData = new FormData();

  formData.append("question", question);
  formData.append("duration", duration.toString());
  formData.append("audio", audio);

  const response = await api.post(
    "/analysis/answer",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};