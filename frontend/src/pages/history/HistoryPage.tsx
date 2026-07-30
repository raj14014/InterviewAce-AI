import { useEffect, useState } from "react";

import { getHistory } from "../../api/history";

import DashboardCard from "../../components/dashboard/DashboardCard";

export default function HistoryPage() {

    const [history, setHistory] = useState<any[]>([]);

    useEffect(() => {

        loadHistory();

    }, []);

    const loadHistory = async () => {

        try {

            const data = await getHistory();

            setHistory(data);

        }

        catch (err) {

            console.error(err);

        }

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
                    marginBottom: 30,
                }}
            >
                Interview History
            </h1>

            {

                history.length === 0 ?

                    (

                        <DashboardCard title="History">

                            <p>No Interview Found.</p>

                        </DashboardCard>

                    )

                    :

                    history.map((item) => (

                        <div
                            key={item.id}
                            style={{
                                marginBottom: 20,
                            }}
                        >

                            <DashboardCard
                                title={`Interview #${item.id}`}
                            >

                                <p><b>Date :</b> {item.date}</p>

                                <p><b>Question :</b> {item.question}</p>

                                <p><b>Score :</b> {item.score}</p>

                                <p><b>Confidence :</b> {item.confidence}</p>

                                <p><b>Communication :</b> {item.communication}</p>

                                <p><b>Emotion :</b> {item.emotion}</p>

                            </DashboardCard>

                        </div>

                    ))

            }

        </div>

    );

}