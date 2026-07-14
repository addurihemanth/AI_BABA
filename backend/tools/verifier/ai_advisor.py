"""
AI_BABA Intelligent Advisor

Converts verification results into
developer recommendations.
"""


class AIAdvisor:


    def generate_advice(
        self,
        reports
    ):

        advice = []


        for report in reports:


            if report.success:

                advice.append(
                    f"{report.name}: Healthy"
                )

            else:

                advice.append(
                    self._generate_fix(
                        report
                    )
                )


        return advice



    def _generate_fix(
        self,
        report
    ):


        mapping = {

            "Project Structure":
                "Create missing enterprise folders",

            "Python Syntax":
                "Fix Python syntax errors before deployment",

            "Configuration":
                "Add required environment configuration",

            "Security Scan":
                "Move secrets into environment variables",

            "Dependencies":
                "Update dependency management",

        }


        return mapping.get(
            report.name,
            f"Review {report.name}"
        )