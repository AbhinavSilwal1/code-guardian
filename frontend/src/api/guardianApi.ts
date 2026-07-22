import type { AnalysisResponse } from "../types/guardian";


const API_URL = "http://127.0.0.1:8000";


export async function analyzeProject(
    path: string
): Promise<AnalysisResponse> {

    const url =
        `${API_URL}/api/analyze?path=${encodeURIComponent(path)}`;

    console.log(
        "Request URL:",
        url
    );


    const response = await fetch(
        url,
        {
            method: "POST",
        }
    );


    console.log(
        "Response status:",
        response.status
    );


    if (!response.ok) {

        const errorText =
            await response.text();

        console.error(
            "API Error:",
            response.status,
            errorText
        );

        throw new Error(
            `HTTP ${response.status}: ${errorText}`
        );
    }


    return response.json();
}