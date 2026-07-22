import IssueRow from "./IssueRow";
import type { Issue } from "../types/guardian";


type IssuesTableProps = {
    issues: Issue[];
};


function IssuesTable({
    issues,
}: IssuesTableProps) {

    return (
        <section className="mt-8 overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm">

            <div className="border-b border-slate-200 px-6 py-5">

                <div className="flex items-center justify-between">

                    <div>

                        <h2 className="text-lg font-semibold text-slate-900">
                            Issues Detected
                        </h2>

                        <p className="mt-1 text-sm text-slate-500">
                            Problems identified during static analysis.
                        </p>

                    </div>

                    <span className="rounded-full bg-slate-100 px-3 py-1 text-sm font-medium text-slate-600">
                        {issues.length}{" "}
                        {issues.length === 1
                            ? "issue"
                            : "issues"
                        }
                    </span>

                </div>

            </div>


            {issues.length === 0 ? (

                <div className="px-6 py-12 text-center">

                    <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-emerald-100 text-xl">
                        ✓
                    </div>

                    <h3 className="mt-4 font-semibold text-slate-900">
                        No issues found
                    </h3>

                    <p className="mt-1 text-sm text-slate-500">
                        CodeGuardian did not detect any problems in this project.
                    </p>

                </div>

            ) : (

                <div className="overflow-x-auto">

                    <table className="w-full text-left">

                        <thead className="bg-slate-50">

                            <tr className="border-b border-slate-200 text-xs font-semibold uppercase tracking-wider text-slate-500">

                                <th className="px-6 py-4">
                                    Category
                                </th>

                                <th className="px-6 py-4">
                                    Severity
                                </th>

                                <th className="px-6 py-4">
                                    File
                                </th>

                                <th className="px-6 py-4">
                                    Line
                                </th>

                            </tr>

                        </thead>


                        <tbody className="divide-y divide-slate-100">

                            {issues.map(
                                (issue, index) => (

                                    <IssueRow
                                        key={index}
                                        issue={issue}
                                    />

                                )
                            )}

                        </tbody>

                    </table>

                </div>

            )}

        </section>
    );
}


export default IssuesTable;