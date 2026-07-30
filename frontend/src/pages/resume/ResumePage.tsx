import { useState } from "react";
import { useNavigate } from "react-router-dom";
import DashboardCard from "../../components/dashboard/DashboardCard";

const API = "http://127.0.0.1:8000";

export default function ResumePage() {

  const navigate = useNavigate();

  const [resume, setResume] = useState<any>(null);

  const [loading, setLoading] = useState(false);

  const uploadResume = async (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {

    if (!e.target.files?.length) return;

    setLoading(true);

    const form = new FormData();

    form.append(
      "file",
      e.target.files[0]
    );

    const response = await fetch(

      `${API}/resume/upload`,

      {

        method: "POST",

        body: form,

      }

    );

    const data = await response.json();

    setResume(data.resume);

    setLoading(false);

  };

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
        }}
      >
        Resume Upload
      </h1>

      <DashboardCard title="Upload Resume">

        <input
          type="file"
          accept=".pdf"
          onChange={uploadResume}
        />

      </DashboardCard>

      {

        loading &&

        <h3>Parsing Resume...</h3>

      }

      {

        resume &&

        <>

          <DashboardCard title="Resume Details">

            <pre>

              {

                JSON.stringify(
                  resume,
                  null,
                  2
                )

              }

            </pre>

          </DashboardCard>

          <button

            onClick={() => navigate("/interview")}

            style={{

              marginTop: 20,

              padding: "15px 35px",

              background: "#38bdf8",

              color: "white",

              border: "none",

              borderRadius: 10,

              cursor: "pointer",

              fontSize: 18,

            }}

          >

            Start AI Interview

          </button>

        </>

      }

    </div>

  );

}