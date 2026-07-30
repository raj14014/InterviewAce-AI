import { Radar } from "react-chartjs-2";

import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
);

type Props = {
  confidence: number;
  communication: number;
  fluency: number;
};

export default function RadarChart({
  confidence,
  communication,
  fluency,
}: Props) {
  const data = {
    labels: [
      "Confidence",
      "Communication",
      "Fluency",
    ],
    datasets: [
      {
        label: "Interview Score",
        data: [
          confidence,
          communication,
          fluency,
        ],
        backgroundColor: "rgba(56,189,248,0.3)",
        borderColor: "#38bdf8",
        borderWidth: 2,
      },
    ],
  };

  return (
    <Radar
      data={data}
      options={{
        responsive: true,
        scales: {
          r: {
            min: 0,
            max: 100,
          },
        },
      }}
    />
  );
}