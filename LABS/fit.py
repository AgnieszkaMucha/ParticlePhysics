import sys  # Import the sys(tem) library for arguments
import ROOT # Import the ROOT library for many uses
 
# Check that the user gave the correct number of arguments
if len(sys.argv) != 3: 
    # Wrong number of arguments, tell the user what you expected
    # Note that sys.argv[0] is how the user called the python script
    print "USAGE: %s <input histogram file> <output plot file>"%(sys.argv[0])
    # End the program
    sys.exit(1)

# Store the user arguments
histFileName = sys.argv[1]
plotFileName = sys.argv[2]

# Retrieve the data histogram from the file
# Open the file in read-only mode
histFile  = ROOT.TFile.Open(histFileName,"READ")
# Get the data histogram
dataHisto = histFile.Get("data")
# Make sure you got the histogram
if not dataHisto:
    print "Failed to get data histogram from the input file"
    sys.exit(1)
# Set the histogram to continue to exist after closing the file
dataHisto.SetDirectory(0)
# Close the input histogram file
histFile.Close()


# Basic style
# Turn off the statistics box
dataHisto.SetStats(0)
# Set the line color to red for MC and black for data
dataHisto.SetLineColor(ROOT.kBlack)
# Set the line width to 2 for MC and data
dataHisto.SetLineWidth(2)
# Set axis labels
dataHisto.GetYaxis().SetTitle("Number of events")
dataHisto.GetXaxis().SetTitle("m_{ll} [MeV]")


# Prepare the canvas for plotting
# Make a canvas
canvas = ROOT.TCanvas("canvas")
# Move into the canvas (so anything drawn is part of this canvas)
canvas.cd()
# Set the y-axis to be logarithmic
canvas.SetLogy(True)


# Open the canvas for continuous printing
# This works for a few file types, most notably pdf files
# This allows you to put several plots in the same pdf file
# The key is the opening square-bracket after the desired file name
canvas.Print(plotFileName+"[")

# Draw the data histogram, as data Points with Errors
dataHisto.Draw("pe")
# Write the data histogram plot to the output file
canvas.Print(plotFileName)

# Fit a Gaussian to the histogram
# "gaus" is one of the built-in fit types
# Fit in the range of 81 to 101 GeV (near the Z-peak)
gaussFit = ROOT.TF1("gaussfit","gaus",81.e3,101.e3)
# Fit the function to the histogram using improved Error (uncertainty) treatment
dataHisto.Fit(gaussFit,"E")
dataHisto.Draw("pe")

# Add the fit results to the plot
# Create the TLatex object
latex = ROOT.TLatex()
# Set the coordinates to be percent-based
latex.SetNDC()
latex.SetTextSize(0.03)
# Get the chi2/ndof
chi2 = gaussFit.GetChisquare()
ndof = gaussFit.GetNDF()
# Draw the mean, width, and chi2/ndof
latex.DrawText(0.5,0.80,"Mean = %.1f GeV"%(gaussFit.GetParameter(1)/1000))
latex.DrawText(0.5,0.75,"Width = %.1f GeV"%(gaussFit.GetParameter(0)/1000))
latex.DrawText(0.5,0.7,"chi2/ndof = %.1f/%d = %.1f"%(chi2,ndof,chi2/ndof))
# Write the plot to the output file
canvas.Print(plotFileName)


# That didn't work very well
# Try fitting a relativistic Breit-Wigner to the Z peak
# This is a more complicated function
# Parameters are [#]
#   [0] is the mass
#   [1] is the width
#   [2] is a normalization factor
# The value to evaluate the function at is x (the mll value in our case)
k_num   = "2*sqrt(2)*[0]*[1]*sqrt([0]*[0]*([0]*[0]+[1]*[1]))"
k_denom = "3.14159*sqrt([0]*[0] + sqrt([0]*[0]*([0]*[0]+[1]*[1])))"
denom   = "((x*x-[0]*[0])*(x*x-[0]*[0]) + [0]*[0]*[1]*[1])"
# I am using python string manipulation syntax to merge the above three lines
# Fit in the full range, as the Breit-Wigner should be more correct
bwFit = ROOT.TF1("bwfit","[2]*(%s/%s)/%s"%(k_num,k_denom,denom),50.e3,200.e3)
# Give the function some help by setting initial values
bwFit.SetParameter(0,100.e3) # Start with a mass of 100 GeV
bwFit.SetParameter(1,1.e3)   # Start with a width of 1 GeV
# Fit the function to the histogram including improved Error (uncertainty) treatment
dataHisto.Fit(bwFit,"E")
dataHisto.Draw("pe")
# Get the chi2/ndof
chi2 = bwFit.GetChisquare()
ndof = bwFit.GetNDF()
# Draw the mass, width, and chi2/ndof
latex.DrawText(0.5,0.80,"Mean = %.1f GeV"%(bwFit.GetParameter(0)/1000))
latex.DrawText(0.5,0.75,"Width = %.1f GeV"%(bwFit.GetParameter(1)/1000))
latex.DrawText(0.5,0.7,"chi2/ndof = %.1f/%d = %.1f"%(chi2,ndof,chi2/ndof))
# Write the plot to the output file
canvas.Print(plotFileName)

# The data and fit agree reasonably well in the core, but not the tails
# Let's plot their ratio to get a better feeling for their agreement
# This is done using a pair of "pads" on the same "canvas"
# For a much more advanced ratio plot, see:
#   https://root.cern.ch/root/html/tutorials/hist/ratioplot.C.html

# Calculate the ratio
# First clone the current data points
ratio = dataHisto.Clone()
# Divide the data points by the fit
ratio.Divide(bwFit)
# Set the line colour to be red to stand out
ratio.SetLineColor(ROOT.kRed)

# Draw the normal plots (not the ratio)
pad1 = ROOT.TPad("pad1","pad1",0,0.3,1,1)
pad1.SetLogy(True)                      # Set the y-axis of the top plot to be logarithmic
pad1.SetBottomMargin(0)                 # Upper and lower pads are joined
pad1.Draw()                             # Draw the upper pad in the canvas
pad1.cd()                               # pad1 becomes the current pad
dataHisto.SetTitle("")                  # Remove the plot title
dataHisto.GetXaxis().SetLabelSize(0)    # Remove x-axis labels for the top pad
dataHisto.GetXaxis().SetTitleSize(0)    # Remove x-axis title for the top pad
dataHisto.GetYaxis().SetTitleSize(0.05) # Increase y-axis title size (pad is not full page)
dataHisto.Draw("pe,same")               # Draw the data points on top of the MC histo

# Add a legend to the top pad
legend = ROOT.TLegend(0.7,0.6,0.85,0.75)    # Add a legend near the top right corner
legend.AddEntry(dataHisto,"Data")           # Add the data points, labelled as "Data"
legend.AddEntry(bwFit,"Breit-Wigner Fit")   # Add the fit, labelled as a Breit-Wigner
legend.SetLineWidth(0)                      # Remove the boundary on the legend
legend.Draw("same")                         # Draw the legend on the plot

# Add other labels with TLatex
# Note that TLatex is global, not pad-related
# As such, the percent-based coordinates for TLatex and the above legend are not the same
latex.SetTextSize(0.06)                     # Increase the text size
latex.DrawText(0.7,0.83,"HASCO 2018")       # Write a label for HASCO
latex.SetTextSize(0.04)                     # Reduce the text size
latex.DrawText(0.7,0.77,"Di-muon events")   # Add a label for the selection

# Draw the mass, width, and chi2/ndof
latex.DrawText(0.4,0.80,"Mean = %.1f GeV"%(bwFit.GetParameter(0)/1000))
latex.DrawText(0.4,0.75,"Width = %.1f GeV"%(bwFit.GetParameter(1)/1000))
latex.DrawText(0.4,0.7,"chi2/ndof = %.1f/%d = %.1f"%(chi2,ndof,chi2/ndof))

# Now draw the ratio
canvas.cd()                 # Go back to the main canvas before defining pad2
pad2 = ROOT.TPad("pad2","pad2",0,0.05,1,0.3)
pad2.SetTopMargin(0)                    # Upper and lower pads are joined
pad2.SetBottomMargin(0.25)              # Expand the bottom margin for extra label space
pad2.Draw()                             # Draw the lower pad in the canvas
pad2.cd()                               # pad2 becomes the current pad
ratio.SetTitle("")                      # Turn off the title to avoid overlap
ratio.GetXaxis().SetLabelSize(0.12)     # Larger x-axis labels (pad is not full page)
ratio.GetXaxis().SetTitleSize(0.12)     # Larger x-axis title (pad is not full page)
ratio.GetYaxis().SetLabelSize(0.1)      # Larger y-axis labels (pad is not full page)
ratio.GetYaxis().SetTitleSize(0.15)     # Larger y-axis title (pad is not full page)
ratio.GetYaxis().SetTitle("Data/Fit")   # Change the y-axis title (this is the ratio)
ratio.GetYaxis().SetTitleOffset(0.3)    # Reduce the y-axis title spacing
ratio.GetYaxis().SetRangeUser(0.5,1.5)  # Set the y-axis ratio range from 0.5 to 1.5
ratio.GetYaxis().SetNdivisions(207)     # Change the y-axis tick-marks to work better
ratio.SetMarkerStyle(3)                 # Change the marker style to stars
ratio.SetMarkerColor(ROOT.kRed)         # Change the marker colour to red
ratio.Draw("pe")                        # Draw the ratio in the current pad, without errors

# Add a line at 1 to the ratio plot
line = ROOT.TLine(50.e3,1,200.e3,1) # Draw a line at 1 from 50 GeV to 200 GeV (full plot)
line.SetLineColor(ROOT.kBlack)      # Set the line colour to black
line.SetLineWidth(2)                # Set the line width to 2
line.Draw("same")                   # Draw the line on the same plot as the ratio

# Write the ratio plot to the output plot file
canvas.Print(plotFileName)

# We're done adding additional plots to the output file
# Close the output file
# The key is the closing square-bracket after the desired file name
canvas.Print(plotFileName + "]")


