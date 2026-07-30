import { ReactMediaRecorder } from "react-media-recorder";
import { submitAnswer } from "../../api/analysis";

type Props = {
  question: string;
  onResult: (result: any) => void;
  onNextQuestion: (question: string) => void;
};

export default function Recorder({
  question,
  onResult,
  onNextQuestion,
}: Props) {
  return (
    <ReactMediaRecorder
      audio
      onStop={async (_, blob) => {
        try {
          const file = new File(
            [blob],
            "answer.wav",
            {
              type: blob.type,
            }
          );

          const result = await submitAnswer(
            question,
            5,
            file
          );

          // Show AI report
          onResult(result);

          // Move to next question
          if (result.next_question) {
            onNextQuestion(result.next_question);
          } else {
            onNextQuestion("Interview Finished.");
          }

        } catch (err) {
          console.error(err);
          alert("Upload Failed");
        }
      }}
      render={({
        status,
        startRecording,
        stopRecording,
        mediaBlobUrl,
      }) => (
        <div
          style={{
            background: "#1e293b",
            padding: 20,
            borderRadius: 12,
          }}
        >
          <h2>Voice Recorder</h2>

          <p>Status: {status}</p>

          <button
            onClick={startRecording}
            style={{
              padding: "10px 20px",
              marginRight: 10,
            }}
          >
            Start Recording
          </button>

          <button
            onClick={stopRecording}
            style={{
              padding: "10px 20px",
            }}
          >
            Stop Recording
          </button>

          {mediaBlobUrl && (
            <div style={{ marginTop: 20 }}>
              <audio controls src={mediaBlobUrl} />
            </div>
          )}
        </div>
      )}
    />
  );
}