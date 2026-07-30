import { useEffect, useState } from "react";
import { getQuestion } from "../../api/analysis";
import Recorder from "../../components/interview/Recorder";
import DashboardCard from "../../components/dashboard/DashboardCard";
import StatCard from "../../components/dashboard/StatCard";
import RadarChart from "../../components/charts/RadarChart";
import jsPDF from "jspdf";

const TOTAL_QUESTIONS = 5;

export default function InterviewPage() {

  const [question, setQuestion] = useState("Loading question...");
  const [result, setResult] = useState<any>(null);

  const [currentQuestion, setCurrentQuestion] = useState(1);

  const [seconds, setSeconds] = useState(0);

  const [finished, setFinished] = useState(false);

  useEffect(() => {

    loadQuestion();

    const timer = setInterval(() => {

      setSeconds((s) => s + 1);

    }, 1000);

    return () => clearInterval(timer);

  }, []);

  const loadQuestion = async () => {

    try {

      const data = await getQuestion();

      setQuestion(data.question);

    } catch {

      setQuestion("Failed to load question.");

    }

  };

  const handleResult = (data: any) => {

    setResult(data);

  };

  const handleNextQuestion = (nextQuestion: string) => {

    if (nextQuestion === "Interview Finished.") {

      setFinished(true);

      return;

    }

    setQuestion(nextQuestion);

    setCurrentQuestion((prev) =>
      Math.min(prev + 1, TOTAL_QUESTIONS)
    );

    setResult(null);

  };

  const downloadReport = () => {

    if (!result) return;

    const pdf = new jsPDF();

    pdf.setFontSize(22);
    pdf.text("InterviewAce AI Report", 20, 20);

    pdf.setFontSize(14);

    pdf.text(`Question:`, 20, 40);
    pdf.text(result.question || "", 20, 50, {
      maxWidth: 170,
    });

    pdf.text("Transcript:", 20, 70);

    pdf.text(
      result.answer || "",
      20,
      80,
      {
        maxWidth: 170,
      }
    );

    pdf.text(
      `Confidence : ${result.voice?.confidence_score}%`,
      20,
      120
    );

    pdf.text(
      `Words : ${result.voice?.words}`,
      20,
      130
    );

    pdf.text(
      `Speed : ${result.voice?.wpm} WPM`,
      20,
      140
    );

    pdf.text(
      `Rating : ${result.voice?.rating}`,
      20,
      150
    );

    pdf.text(
      "AI Feedback:",
      20,
      170
    );

    pdf.setFontSize(11);

    pdf.text(

      typeof result.evaluation === "string"
        ? result.evaluation
        : JSON.stringify(result.evaluation, null, 2),

      20,

      180,

      {
        maxWidth: 170,
      }

    );

    pdf.save("Interview_Report.pdf");

  };

  if (finished) {

    return (

      <div
        style={{
          background: "#0f172a",
          color: "white",
          minHeight: "100vh",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
        }}
      >

        <h1>🎉 Interview Completed</h1>

        <h2>Total Time</h2>

        <h1>

          {Math.floor(seconds / 60)}:

          {(seconds % 60)
            .toString()
            .padStart(2, "0")}

        </h1>

        <p>

          Thank you for completing the AI Interview.

        </p>

      </div>

    );

  }

  return (

    <div
      style={{
        background: "#0f172a",
        minHeight: "100vh",
        padding: 40,
        color: "white",
      }}
    >

      <h1
        style={{
          color: "#38bdf8",
          marginBottom: 30,
        }}
      >
        InterviewAce AI
      </h1>

      <div style={{ marginBottom: 30 }}>

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            marginBottom: 10,
          }}
        >

          <h3>

            Question {currentQuestion} / {TOTAL_QUESTIONS}

          </h3>

          <h3>

            {Math.floor(seconds / 60)}:

            {(seconds % 60)
              .toString()
              .padStart(2, "0")}

          </h3>

        </div>

        <div
          style={{
            width: "100%",
            height: 10,
            background: "#334155",
            borderRadius: 20,
          }}
        >

          <div
            style={{
              width: `${(currentQuestion / TOTAL_QUESTIONS) * 100}%`,
              height: 10,
              background: "#38bdf8",
              borderRadius: 20,
              transition: "0.4s",
            }}
          />

        </div>

      </div>

      <DashboardCard title="Current Interview Question">

        <div
          style={{
            fontSize: 24,
            fontWeight: 600,
          }}
        >

          {question}

        </div>

      </DashboardCard>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: 20,
          marginTop: 25,
        }}
      >

        <DashboardCard title="Voice Recorder">

          <Recorder
            question={question}
            onResult={handleResult}
            onNextQuestion={handleNextQuestion}
          />

        </DashboardCard>

        <DashboardCard title="Live AI Analysis">

          {result ? (

            <>
              <p><b>Words:</b> {result.voice?.words}</p>
              <p><b>Speed:</b> {result.voice?.wpm} WPM</p>
              <p><b>Fillers:</b> {result.voice?.fillers}</p>
              <p><b>Confidence:</b> {result.voice?.confidence_score}%</p>
              <p><b>Rating:</b> {result.voice?.rating}</p>
            </>

          ) : (

            <p>Waiting for recording...</p>

          )}

        </DashboardCard>

      </div>

      {result && (

        <>

          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(3,1fr)",
              gap: 20,
              marginTop: 30,
            }}
          >

            <StatCard
              title="Confidence"
              value={`${result.voice?.confidence_score}%`}
            />

            <StatCard
              title="Communication"
              value={result.voice?.rating}
            />

            <StatCard
              title="Words"
              value={result.voice?.words}
            />

          </div>

          <div style={{ marginTop: 30 }}>

            <DashboardCard title="AI Feedback">

              <pre
                style={{
                  whiteSpace: "pre-wrap",
                  color: "#7dd3fc",
                }}
              >

                {typeof result.evaluation === "string"
                  ? result.evaluation
                  : JSON.stringify(result.evaluation, null, 2)}

              </pre>

            </DashboardCard>

          </div>

          <div style={{ marginTop: 30 }}>

            <DashboardCard title="Transcript">

              <p>{result.answer}</p>

            </DashboardCard>

          </div>

          <div style={{ marginTop: 30 }}>

            <DashboardCard title="Performance Radar">

              <RadarChart
                confidence={result.voice?.confidence_score || 0}
                communication={90}
                fluency={result.voice?.confidence_score || 0}
              />

            </DashboardCard>

          </div>

          <div
            style={{
              marginTop: 30,
              textAlign: "center",
            }}
          >

            <button
              onClick={downloadReport}
              style={{
                padding: "12px 30px",
                background: "#38bdf8",
                color: "white",
                border: "none",
                borderRadius: 8,
                fontSize: 18,
                cursor: "pointer",
              }}
            >
              Download Interview Report PDF
            </button>

          </div>

        </>

      )}

    </div>

  );

}