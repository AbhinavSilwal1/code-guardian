import Header from "./components/Header";
import IssuesTable from "./components/IssuesTable";
import StatCard from "./components/StatCard";

function App() {
    return (
        <main className="min-h-screen bg-slate-100">
            <div className="mx-auto max-w-7xl p-8">
                <Header />

                <section className="mb-8 grid gap-6 md:grid-cols-2 lg:grid-cols-5">
                    <StatCard title="Files Scanned" value={0} />
                    <StatCard title="Total Issues" value={0} />
                    <StatCard title="High" value={0} />
                    <StatCard title="Medium" value={0} />
                    <StatCard title="Low" value={0} />
                </section>

                <IssuesTable />
            </div>
        </main>
    );
}

export default App;