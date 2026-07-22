type StatCardProps = {
    title: string;
    value: number;
    variant?: "default" | "high" | "medium" | "low";
};


function StatCard({
    title,
    value,
    variant = "default",
}: StatCardProps) {

    const variantStyles = {
        default: "border-slate-200",
        high: "border-red-200",
        medium: "border-amber-200",
        low: "border-emerald-200",
    };


    const valueStyles = {
        default: "text-slate-900",
        high: "text-red-600",
        medium: "text-amber-600",
        low: "text-emerald-600",
    };


    return (
        <div
            className={`rounded-2xl border bg-white p-6 shadow-sm transition hover:-translate-y-1 hover:shadow-md ${variantStyles[variant]}`}
        >

            <p className="text-sm font-medium text-slate-500">
                {title}
            </p>

            <p
                className={`mt-3 text-3xl font-bold ${valueStyles[variant]}`}
            >
                {value}
            </p>

        </div>
    );
}


export default StatCard;