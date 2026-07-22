import type { AnalysisResponse } from "../types/guardian";


const API_URL = "http://127.0.0.1:8000";


export async function analyzeProject(
    path: string
): Promise<AnalysisResponse> {

    const url =
        `${API_URL}/api/analyze?path=${encodeURIComponent(path)}`;


    const response = await fetch(
        url,
        {
            method: "POST",
        }
    );


    if (!response.ok) {

        let message =
            "An unexpected error occurred while analyzing the project.";


        try {

            const errorData =
                await response.json();


            if (
                typeof errorData.detail === "string"
            ) {
                message =
                    errorData.detail;
            }

        } catch {

            message =
                "Unable to analyze the project.";
        }


        throw new Error(message);
    }


    return response.json();
}