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

export const sendRequest = (data, route) => {
    return fetch(route, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRF-TOKEN': document.querySelector('meta[name="csrf-token"]').getAttribute('content'),
        },
    }).then(response => response.json())
}