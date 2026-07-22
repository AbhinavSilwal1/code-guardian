type AnalysisSummaryProps = {
    path: string;
    duration: number | null;
    lastAnalyzed: Date | null;
};


function AnalysisSummary({
    path,
    duration,
    lastAnalyzed,
}: AnalysisSummaryProps) {

    return (
        <section className="mb-8 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

            <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">

                {/* Project Information */}

                <div className="min-w-0">

                    <p className="text-sm font-medium text-slate-500">
                        Analysis Results
                    </p>

                    <h2 className="mt-1 truncate text-xl font-semibold text-slate-900">
                        {path}
                    </h2>

                </div>


                {/* Analysis Metadata */}

                <div className="flex flex-wrap gap-3">

                    {duration !== null && (

                        <div className="rounded-xl bg-slate-50 px-4 py-3">

                            <p className="text-xs font-medium uppercase tracking-wide text-slate-500">
                                Analysis Time
                            </p>

                            <p className="mt-1 text-sm font-semibold text-slate-800">
                                {duration.toFixed(2)}s
                            </p>

                        </div>

                    )}


                    {lastAnalyzed !== null && (

                        <div className="rounded-xl bg-slate-50 px-4 py-3">

                            <p className="text-xs font-medium uppercase tracking-wide text-slate-500">
                                Last Analyzed
                            </p>

                            <p className="mt-1 text-sm font-semibold text-slate-800">
                                {lastAnalyzed.toLocaleTimeString()}
                            </p>

                        </div>

                    )}

                </div>

            </div>

        </section>
    );
}


export default AnalysisSummary;