
export const sendGetRequest = async (url) => {
    const response = await fetch(`${process.env.REACT_APP_FETCH_URL}${url}`);
    const data = await response.json();
    return data;
}