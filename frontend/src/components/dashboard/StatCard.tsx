type Props = {
  title: string;
  value: string | number;
};

export default function StatCard({
  title,
  value,
}: Props) {

  return (
    <div
      style={{
        background:"#1e293b",
        padding:20,
        borderRadius:15,
        textAlign:"center",
      }}
    >
      <h3>{title}</h3>

      <h1
        style={{
          color:"#38bdf8",
        }}
      >
        {value}
      </h1>
    </div>
  );
}