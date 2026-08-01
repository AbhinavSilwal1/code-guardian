type RepositoryInfoProps = {
    source: {
        type: string | null;
        owner: string | null;
        repository: string | null;
        url: string | null;
    } | null;
};


function RepositoryInfo({source,}: RepositoryInfoProps) {

    if (
        !source ||
        source.type !== "github"
    ) {
        return null;
    }


    return (

        <section className="mb-6 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

            <h3 className="text-lg font-semibold text-slate-900">
                Repository Information
            </h3>

            <div className="mt-4 space-y-2 text-sm text-slate-700">

                <p>
                    <span className="font-semibold">
                        Owner:
                    </span>{" "}
                    {source.owner}
                </p>

                <p>
                    <span className="font-semibold">
                        Repository:
                    </span>{" "}
                    {source.repository}
                </p>

                <p>
                    <span className="font-semibold">
                        URL:
                    </span>{" "}
                    <a
                        href={source.url ?? ""}
                        target="_blank"
                        rel="noreferrer"
                        className="text-blue-600 hover:underline"
                    >
                        {source.url}
                    </a>
                </p>

            </div>

        </section>

    );

}


export default RepositoryInfo;