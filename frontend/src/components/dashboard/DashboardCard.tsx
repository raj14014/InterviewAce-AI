type Props = {
  title: string;
  children: React.ReactNode;
};

export default function DashboardCard({
  title,
  children,
}: Props) {
  return (
    <div
      style={{
        background: "#1e293b",
        borderRadius: 15,
        padding: 20,
        boxShadow: "0 0 12px rgba(0,0,0,.3)",
      }}
    >
      <h2
        style={{
          marginBottom: 20,
          color: "#38bdf8",
        }}
      >
        {title}
      </h2>

      {children}
    </div>
  );
}