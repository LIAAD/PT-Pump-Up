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

export const handleTextFieldChange = (event, state, setState) => {
    setState({
        ...state,
        [event.target.name]: event.target.value
    })
}