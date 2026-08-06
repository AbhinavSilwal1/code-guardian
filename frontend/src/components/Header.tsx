import logo from "../assets/code_guardian_logo.png";


function Header() {
    return (
        <header className="mb-10">

            <div className="flex items-center gap-4">

                <img
                    src={logo}
                    alt="CodeGuardian Logo"
                    className="
                        h-14
                        w-14
                        rounded-2xl
                        object-cover
                        shadow-lg
                    "
                />

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