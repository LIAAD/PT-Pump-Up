
export const sendGetRequest = async (url) => {
    try {
        const response = await fetch(`${process.env.REACT_APP_FETCH_URL}${url}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
        });
        return await response.json();
    } catch (error) {
        return error;
    }
};
