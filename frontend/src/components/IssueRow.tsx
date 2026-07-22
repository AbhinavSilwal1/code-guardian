import { useState } from "react";
import type { Issue } from "../types/guardian";


type IssueRowProps = {
    issue: Issue;
};


function IssueRow({
    issue,
}: IssueRowProps) {

    const [expanded, setExpanded] =
        useState(false);


    const severityStyles: Record<
        string,
        string
    > = {

        HIGH:
            "bg-red-100 text-red-700",

        MEDIUM:
            "bg-amber-100 text-amber-700",

        LOW:
            "bg-emerald-100 text-emerald-700",

    };


    const severityStyle =
        severityStyles[
            issue.severity.toUpperCase()
        ]
        ??
        "bg-slate-100 text-slate-700";


    return (
        <>
            {/* Issue Row */}

            <tr
                onClick={() =>
                    setExpanded(!expanded)
                }
                className={`
                    cursor-pointer
                    border-t border-slate-200
                    transition
                    ${
                        expanded
                            ? "bg-slate-50"
                            : "hover:bg-slate-50"
                    }
                `}
            >

                <td className="px-4 py-3 font-medium text-slate-700">
                    {issue.category}
                </td>


                <td className="px-4 py-3">

                    <span
                        className={`
                            inline-flex rounded-full
                            px-3 py-1 text-xs font-semibold
                            ${severityStyle}
                        `}
                    >
                        {issue.severity}
                    </span>

                </td>


                <td className="px-4 py-3 text-slate-600">
                    {issue.file}
                </td>


                <td className="px-4 py-3">

                    <div className="flex items-center justify-between">

                        <span className="text-slate-600">
                            {issue.line ?? "—"}
                        </span>


                        <div className="relative ml-4">

                            <span
                                className="
                                    text-sm
                                    font-medium
                                    text-slate-400
                                    transition
                                    group-hover:text-slate-600
                                "
                            >
                                {expanded
                                    ? "▲"
                                    : "▼"
                                }
                            </span>

                        </div>

                    </div>

                </td>

            </tr>


            {/* Expanded Details */}

            {expanded && (

                <tr className="bg-slate-50">

                    <td
                        colSpan={4}
                        className="px-6 py-6"
                    >

                        <div className="space-y-5">

                            {/* Message */}

                            <div>

                                <p className="text-xs font-semibold uppercase tracking-wide text-slate-500">
                                    Message
                                </p>

                                <div className="mt-2 rounded-lg border border-slate-200 bg-white p-4">

                                    <p className="text-sm leading-6 text-slate-700">
                                        {issue.message}
                                    </p>

                                </div>

                            </div>


                            {/* Suggestion */}

                            {issue.suggestion && (

                                <div>

                                    <p className="text-xs font-semibold uppercase tracking-wide text-slate-500">
                                        Suggestion
                                    </p>

                                    <div className="mt-2 rounded-lg border border-blue-200 bg-blue-50 p-4">

                                        <p className="text-sm leading-6 text-blue-800">
                                            💡 {issue.suggestion}
                                        </p>

                                    </div>

                                </div>

                            )}

                        </div>

                    </td>

                </tr>

            )}

        </>
    );
}


export default IssueRow;