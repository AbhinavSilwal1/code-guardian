type StatCardProps = {
    title: string;
    value: number;
};

function StatCard({ title, value }: StatCardProps) {
    return (
        <div className="rounded-xl bg-white p-6 shadow">
            <h2 className="text-sm font-medium text-slate-500">
                {title}
            </h2>

            <p className="mt-2 text-3xl font-bold text-slate-800">
                {value}
            </p>
        </div>
    );
}

export default StatCard;