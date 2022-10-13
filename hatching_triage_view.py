# Copyright (C) 2021-2022 Hatching B.V.
# Recorded Future Sandbox
# All rights reserved.

def _make_tags_dictlist(tags):
    tag_dicts = []
    for t in tags:
        family = False
        if t.startswith("family:"):
            t = t[len("family:"):]
            family = True

        tag_dicts.append({"name": t, "family": family})

    # Sort so that family tags appear first in the list.
    return sorted(tag_dicts, reverse=True, key=lambda d: d["family"])


def _make_report_contexts(result):
    # We use this report context to grab all ttps and tags from all tasks
    # and deduplicate them. This way we create a very small overview report.
    action_results = []
    for action_result in result.get_data():
        report = action_result.get("report")
        if not report:
            continue

        ttps = []
        tags = []
        for taskdata in report.get("tasks", {}).values():
            analysis = taskdata.get("analysis", {})
            if not analysis:
                continue

            analysis_ttps = analysis.get("ttp", [])
            if analysis_ttps:
                ttps.extend(analysis_ttps)

            analysis_tags = analysis.get("tags", [])
            if analysis_tags:
                tags.extend(analysis_tags)

        report["ttps"] = list(set(ttps))
        report["tags"] = _make_tags_dictlist(set(tags))
        action_results.append(action_result)

    return action_results


def do_view(provides, all_app_runs, context):

    context["results"] = results = []
    for summary, action_results in all_app_runs:
        for result in action_results:
            if result:
                results.append(_make_report_contexts(result))

    return "hatching_triage_view.html"
