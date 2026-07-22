type IssueBreakdownProps = {
    categoryCounts: Record<string, number>;
};


function IssueBreakdown({
    categoryCounts,
}: IssueBreakdownProps) {

    const categories =
        Object.entries(categoryCounts)
            .sort(
                ([, countA], [, countB]) =>
                    countB - countA
            );


    return (
        <section className="mb-8 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

            <div className="mb-5">

                <h2 className="text-lg font-semibold text-slate-900">
                    Issue Breakdown
                </h2>

                <p className="mt-1 text-sm text-slate-500">
                    Issues grouped by category.
                </p>

            </div>


            {categories.length === 0 ? (

                <div className="rounded-xl bg-emerald-50 p-5 text-center">

                    <p className="font-medium text-emerald-700">
                        No issues detected.
                    </p>

                    <p className="mt-1 text-sm text-emerald-600">
                        Your project passed all CodeGuardian checks.
                    </p>

                </div>

            ) : (

                <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">

                    {categories.map(
                        ([category, count]) => (

                            <div
                                key={category}
                                className="rounded-xl border border-slate-200 bg-slate-50 p-4 transition hover:border-slate-300 hover:bg-slate-100"
                            >

                                <div className="flex items-center justify-between gap-4">

                                    <p className="truncate text-sm font-medium text-slate-700">
                                        {category}
                                    </p>

                                    <span className="flex h-8 min-w-8 items-center justify-center rounded-full bg-slate-200 px-2 text-sm font-bold text-slate-700">
                                        {count}
                                    </span>

                                </div>

                            </div>

                        )
                    )}

                </div>

            )}

        </section>
    );
}


export default IssueBreakdown;