import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

#df = pd.read_csv('../data/laptop_df.csv')
df = pickle.load(open('df.pkl', 'rb'))
 #df.drop(columns=['Unnamed: 0'], inplace= True)

def show_explore_page():
    st.title("Laptop Price Explorer")

    st.subheader('Dataframe')
    format_rows = st.radio('Format', ['Sample', 'Head', 'Tail'])
    n_rows = st.number_input("Number of rows: ", min_value=1, max_value=df.shape[0])
    df_formating(n_rows, format_rows)

    # boxplot
    st.subheader('Boxplot')
    boxplot_feature = st.radio("Select the feature to see boxplot ", list(df.columns[1:]))
    price_boxplot(boxplot_feature)

    # sunburst
    st.subheader('Sunburst')
    fig = px.sunburst(df[df['manufacturer']!='Apple'], path=['manufacturer', 'graphics_copressor', 'cpu_name'], values='price',
                      title='Price Distribution in Hierarchical Data', width=800, height=800)
    st.write(fig)

    st.subheader('Bar Plot')
    barplot_features = st.radio("Select the feature to see boxplot ", ['manufacturer', 'graphics_copressor', 'cpu_name','os'])
    bar_plot(barplot_features)

    fig = px.bar(df[df['manufacturer']!='Apple'], x='manufacturer', color='graphics_copressor', title='Comparison Between All Manufacturers Among Different GPU Excluding Apple')
    st.write(fig)

    scatter_plot()

    fig = px.scatter(df, x='ppi', y='price', title='Price Vs PPI')
    st.write(fig)

    # correlation
    st.subheader('Heatmap')

    numeric_df = df.select_dtypes(include=['number'])
    correlation = numeric_df.corr()



    # Create a heatmap
    #fig = sns.heatmap(correlation)
    fig = go.Figure(data=go.Heatmap(
         z=correlation.values,
         x=correlation.columns,
         y=correlation.columns,
         colorscale='Viridis'))

    fig.update_layout(title='Correlation')
    st.write(fig)

    #fig, ax = plt.subplots()
    #sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax)
    #plt.title(f"Correlation Heatmap of ")
    #st.pyplot(fig)

    st.write('<style>.row-widget.stRadio div {display: flex;flex-direction:row;}</style>', unsafe_allow_html=True)


def price_boxplot(feature):
    fig = px.box(df, x=feature, y='price', title=f'Price vs {feature.capitalize()} Feature')
    st.write(fig)

def bar_plot(feature):
    fig = px.bar(df, x= feature, title=f'Barplot: {feature.capitalize()}')
    st.write(fig)

def scatter_plot():

    st.subheader('Scatter Plot: ')
    y_axis = st.radio('Y-axis: ', ['cpu_name', 'graphics_copressor'])
    x_axis = st.radio('X-axis: ', ['ram', 'num_processors'])
    color = st.radio('Color: ', ['touchable', 'ips'])

    fig = px.scatter(df, x=x_axis, y=y_axis, color=color, title=f'{x_axis.capitalize()} vs {y_axis.capitalize()}')
    st.write(fig)

def df_formating(n_rows=5.00, format_rows='Sample'):


    if format_rows == 'Sample':
        st.write(df.sample(n_rows))
    elif format_rows == 'Head':
        st.write(df.head(n_rows))
    else:
        st.write(df.tail(n_rows))


