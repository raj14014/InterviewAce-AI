type Props = {
  label: string;
  value: number;
};

export default function ProgressBar({
  label,
  value,
}: Props) {
  return (
    <div
      style={{
        marginBottom: 20,
      }}
    >
      <p>{label}</p>

      <div
        style={{
          width: "100%",
          height: 14,
          background: "#334155",
          borderRadius: 10,
        }}
      >
        <div
          style={{
            width: `${value}%`,
            height: "100%",
            background: "#38bdf8",
            borderRadius: 10,
            transition: "0.8s",
          }}
        />
      </div>

      <p>{value}%</p>
    </div>
  );
}