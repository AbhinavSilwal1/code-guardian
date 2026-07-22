function Header() {
    return (
        <header className="mb-10">

            <div className="flex items-center gap-4">

                <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-slate-900 text-3xl shadow-lg">
                    🛡️
                </div>

                <div>

                    <h1 className="text-4xl font-bold tracking-tight text-slate-900">
                        CodeGuardian
                    </h1>

                    <p className="mt-1 text-sm font-medium text-slate-500">
                        Python static analysis dashboard
                    </p>

                </div>

            </div>

        </header>
    );
}

export default Header;