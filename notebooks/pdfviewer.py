
@flask_app.route('/viewpdf')
@cross_origin()

def view_pdf():
    assets_path = os.path.join(dirname, 'assets')
    filename = request.args['filename']
    file_to_be_sent = open(os.path.join(assets_path, filename), 'rb')
    response = make_response(send_file(file_to_be_sent, as_attachment=False, attachment_filename=filename))
    response.headers['Content-Disposition'] = "inline; filename=%s" %(filename)
    return response, 200

@flask_app.route('/viewpdfsample')
@cross_origin()
def view_pdf_sample():
    filename = 'Ender_Dimension changes of polymers in liquids_Apparatus & First results.pdf'
    return send_from_directory('assets', filename, mimetype='application/pdf')

if __name__ == '__main__':
    print("Starting Flask Server")
    # app.run_server(host='0.0.0.0', port=5000)
    flask_app.run(host="0.0.0.0", port=5000, debug=True)
    