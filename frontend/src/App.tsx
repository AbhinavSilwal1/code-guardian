import { useState } from "react";
import Header from "./components/Header";
import IssuesTable from "./components/IssuesTable";
import StatCard from "./components/StatCard";
import { analyzeProject } from "./api/guardianApi";
import type { AnalysisResponse } from "./types/guardian";


function App() {

    const [path, setPath] = useState("");

    const [data, setData] =
        useState<AnalysisResponse | null>(null);

    const [loading, setLoading] =
        useState(false);

    const [error, setError] =
        useState<string | null>(null);


    async function handleAnalyze() {

        setLoading(true);

        setError(null);

        setData(null);

        try {

            const result =
                await analyzeProject(path);

            setData(result);

        } catch (err) {

            setError(
                err instanceof Error
                    ? err.message
                    : "An unexpected error occurred."
            );

        } finally {

            setLoading(false);

        }
    }


    return (
        <main className="min-h-screen bg-slate-100">

            <div className="mx-auto max-w-7xl p-8">

                <Header />


                {/* Project Analysis Controls */}

                <div className="mb-8 flex gap-4">

                    <input
                        className="flex-1 rounded-lg border p-3"
                        placeholder="Project path..."
                        value={path}
                        onChange={
                            (event) =>
                                setPath(event.target.value)
                        }
                    />


                    <button
                        onClick={handleAnalyze}
                        disabled={loading}
                        className="rounded-lg bg-blue-600 px-6 py-3 font-medium text-white disabled:cursor-not-allowed disabled:opacity-50"
                    >
                        {loading
                            ? "Analyzing..."
                            : "Analyze"
                        }
                    </button>

                </div>


                {/* Error State */}

                {error && (

                    <div className="mb-8 rounded-lg border border-red-200 bg-red-50 p-4 text-red-700">

                        <p className="font-semibold">
                            Analysis Failed
                        </p>

                        <p className="mt-1 text-sm">
                            {error}
                        </p>

                    </div>

                )}


                {/* Loading State */}

                {loading && (

                    <div className="mb-8 rounded-lg bg-white p-6 text-center shadow">

                        <p className="font-medium">
                            Analyzing project...
                        </p>

                        <p className="mt-1 text-sm text-slate-500">
                            Please wait while CodeGuardian scans your project.
                        </p>

                    </div>

                )}


                {/* Analysis Results */}

                {data ? (

                    <>

                        {/* Summary Cards */}

                        <section className="grid gap-6 md:grid-cols-2 lg:grid-cols-5">

                            <StatCard
                                title="Files Scanned"
                                value={
                                    data.summary.files_scanned
                                }
                            />

                            <StatCard
                                title="Issues"
                                value={
                                    data.summary.total_issues
                                }
                            />

                            <StatCard
                                title="High"
                                value={
                                    data.summary.severity_counts?.HIGH ?? 0
                                }
                            />

                            <StatCard
                                title="Medium"
                                value={
                                    data.summary.severity_counts?.MEDIUM ?? 0
                                }
                            />

                            <StatCard
                                title="Low"
                                value={
                                    data.summary.severity_counts?.LOW ?? 0
                                }
                            />

                        </section>


                        {/* Issues Table */}

                        <IssuesTable
                            issues={data.issues}
                        />

                    </>

                ) : (

                    /* Empty State */

                    !loading &&
                    !error && (

                        <div className="rounded-xl bg-white p-8 text-center shadow">

                            <h2 className="text-xl font-semibold">
                                No analysis results yet
                            </h2>

                            <p className="mt-2 text-slate-500">
                                Enter a project path above
                                to begin scanning.
                            </p>

                        </div>

                    )

                )}

            </div>

        </main>
    );
}


export default App;