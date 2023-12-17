export const filterByNLPTask = (response) => {
    const datasetsByTask = {}

    response.forEach(element => {
        element.nlp_tasks.forEach(task => {
            if (task.name in datasetsByTask) {
                datasetsByTask[task.name].push(element)
            } else {
                datasetsByTask[task.name] = [element]
            }
        })
    });

    return datasetsByTask
}