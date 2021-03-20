#include<iostream>          // For printing messages to the terminal
#include<string>            // For strings
#include<TH1D.h>            // ROOT histograms
#include<TFile.h>           // ROOT files
#include<TCanvas.h>         // ROOT canvas for plotting
#include<TPad.h>            // ROOT pads for advanced plotting
#include<TLegend.h>         // ROOT legends for plots
#include<TLatex.h>          // ROOT latex for flexible text drawing
#include<TLine.h>           // ROOT support for drawing lines
#include<TF1.h>             // ROOT functions for fitting

int fit(std::string histFileName, std::string plotFileName)
{
    // Retrieve the data histogram from the file
    // Open the file in read-only mode
    TFile* histFile = TFile::Open(histFileName.c_str(),"READ");
    // Get the data histogram
    TH1D* dataHisto = (TH1D*)histFile->Get("data");
    // Make sure you got the histogram
    if (!dataHisto)
    {
        std::cout << "Failed to get data histogram from the input file" << std::endl;
        exit(1);
    }
    // Set the histogram to continue to exist after closing the file
    dataHisto->SetDirectory(0);
    // Close the input histogram file
    histFile->Close();

    // Basic style
    //  Turn off the statistics box
    dataHisto->SetStats(0);
    // Set the line color to red for MC and black for data
    dataHisto->SetLineColor(kBlack);
    // Set the line width to 2 for MC and data
    dataHisto->SetLineWidth(2);
    // Set axis labels
    dataHisto->GetYaxis()->SetTitle("Number of events");
    dataHisto->GetXaxis()->SetTitle("m_{ll} [MeV]");

    // Prepare the canvas for plotting
    // Make a canvas
    TCanvas canvas("canvas");
    // Move into the canvas (so anything drawn is part of this canvas)
    canvas.cd();
    // Set the y-axis to be logarithmic
    canvas.SetLogy(true);

    
    // Open the canvas for continuous printing
    // This works for a few file types, most notably pdf files
    // This allows you to put several plots in the same pdf file
    // The key is the opening square-bracket after the desired file name
    canvas.Print(Form("%s[",plotFileName.c_str()));

    // Draw the data histogram, as data Points with Errors
    dataHisto->Draw("pe");
    // Write the data histogram plot to the output file
    canvas.Print(plotFileName.c_str());

    // Fit a Gaussian to the histogram
    // "gaus" is one of the built-in fit types
    // Fit in the range of 81 to 101 GeV (near the Z-peak)
    TF1 gaussFit("gaussfit","gaus",81.e3,101.e3);
    //  Fit the function to the histogram including improved Error (uncertainty) treatment
    dataHisto->Fit(&gaussFit,"E");
    dataHisto->Draw("pe");

    // Add the fit results to the plot
    // Create the TLatex object
    TLatex latex;
    // Set the coordinates to be percent-based
    latex.SetNDC();
    latex.SetTextSize(0.03);
    // Get the chi2/ndof
    double chi2 = gaussFit.GetChisquare();
    int ndof = gaussFit.GetNDF();
    // Draw the mean, width, and chi2/ndof
    latex.DrawText(0.5,0.80,Form("Mean = %.1f GeV",gaussFit.GetParameter(1)/1000));
    latex.DrawText(0.5,0.75,Form("Width = %.1f GeV",gaussFit.GetParameter(0)/1000));
    latex.DrawText(0.5,0.7,Form("chi2/ndof = %.1f/%d = %.1f",chi2,ndof,chi2/ndof));
    // Write the plot to the output file
    canvas.Print(plotFileName.c_str());


    // That didn't work very well
    // Try fitting a relativistic Breit-Wigner to the Z peak
    // This is a more complicated function
    // Parameters are [#]
    //  [0] is the mass
    //  [1] is the width
    //  [2] is a normalization factor
    // The value to evaluate the function is at x (the mll value in our case)
    std::string k_num   = "2*sqrt(2)*[0]*[1]*sqrt([0]*[0]*([0]*[0]+[1]*[1]))";
    std::string k_denom = "3.14159*sqrt([0]*[0] + sqrt([0]*[0]*([0]*[0]+[1]*[1])))";
    std::string denom   = "((x*x-[0]*[0])*(x*x-[0]*[0]) + [0]*[0]*[1]*[1])";
    // I am using C++/ROOT string manipulation syntax to merge the above three lines
    // Fit in the full range, as the Breit-Wigner should be more correct
    TF1 bwFit("bwfit",Form("[2]*(%s/%s)/%s",k_num.c_str(),k_denom.c_str(),denom.c_str()),50.e3,200.e3);
    // Give the function some help by setting initial values
    bwFit.SetParameter(0,100.e3);   // Start with a mass of 100 GeV
    bwFit.SetParameter(1,1.e3);     // Start with a width of 1 GeV
    // Fit the function to the histogram including improved Error (uncertainty) treatment
    dataHisto->Fit(&bwFit,"E");
    dataHisto->Draw("pe");
    // Get the chi2/ndof
    chi2 = bwFit.GetChisquare();
    ndof = bwFit.GetNDF();
    // Draw the mass, width, and chi2/ndof
    latex.DrawText(0.5,0.80,Form("Mean = %.1f GeV",bwFit.GetParameter(0)/1000));
    latex.DrawText(0.5,0.75,Form("Width = %.1f GeV",bwFit.GetParameter(1)/1000));
    latex.DrawText(0.5,0.7,Form("chi2/ndof = %.1f/%d = %.1f",chi2,ndof,chi2/ndof));
    // Write the plot to the output file
    canvas.Print(plotFileName.c_str());

    // The data and fit agree reasonably well in the core, but not the tails
    // Let's plot their ratio to get a better feeling for their agreement
    // This is done using a pair of "pads" on the same "canvas"
    // For a much more advanced ratio plot, see:
    //  https://root.cern.ch/root/html/tutorials/hist/ratioplot.C.html

    // Calculate the ratio
    // First clone the current data points
    TH1D* ratio = (TH1D*)dataHisto->Clone();
    // Divide the data points by the fit
    ratio->Divide(&bwFit);
    // Set the line colour to be red to stand out
    ratio->SetLineColor(kRed);

    // Draw the normal plots (not the ratio)
    TPad pad1("pad1","pad1",0,0.3,1,1);
    pad1.SetLogy(true);                     // Set the y-axis of the top plot to be logarithmic
    pad1.SetBottomMargin(0);                // Upper and lower pads are joined
    pad1.Draw();                            // Draw the upper pad in the canvas
    pad1.cd();                              // pad1 becomes the current pad
    dataHisto->SetTitle("");                  // Remove the plot title
    dataHisto->GetXaxis()->SetLabelSize(0);   // Remove x-axis labels for the top pad
    dataHisto->GetXaxis()->SetTitleSize(0);   // Remove x-axis title for t he top pad
    dataHisto->GetYaxis()->SetTitleSize(0.05);// Increase y-axis title size (pad is not full page)
    dataHisto->Draw("pe");             // Draw the data points on top of the MC histo

    // Add a legend to the top pad
    TLegend legend(0.7,0.6,0.85,0.75);      // Add a legend near the top right corner
    legend.AddEntry(dataHisto,"Data");      // Add the data points, labelled as "Data"
    legend.AddEntry(&bwFit,"Breit-Wigner Fit"); // Add the fit, labelled as a Breit-Wigner
    legend.SetLineWidth(0);                 // Remove the boundary on the legend
    legend.Draw("same");                    // Draw the legend on the plot

    // Add other labels with TLatex
    // Note that TLatex is global, not pad-related
    // As such, the percent-based coordinates for TLatex and the above legend are not the same
    latex.SetTextSize(0.06);                    // Increase the text size
    latex.DrawText(0.7,0.83,"HASCO 2018");      // Write a label for HASCO
    latex.SetTextSize(0.04);                    // Reduce the text size
    latex.DrawText(0.7,0.77,"Di-muon events");  // Add a label for the selection
    
    // Draw the mass, width, and chi2/ndof
    latex.DrawText(0.40,0.8,Form("Mean = %.1f GeV",bwFit.GetParameter(0)/1000));
    latex.DrawText(0.40,0.75,Form("Width = %.1f GeV",bwFit.GetParameter(1)/1000));
    latex.DrawText(0.40,0.7,Form("chi2/ndof = %.1f/%d = %.1f",chi2,ndof,chi2/ndof));

    // Now draw the ratio
    canvas.cd();                                // Go back to the main canvas before defining pad2
    TPad pad2("pad2","pad2",0,0.05,1,0.3);
    pad2.SetTopMargin(0);                       // Upper and lower pads are joined
    pad2.SetBottomMargin(0.25);                 // Expand the bottom margin for extra label space
    pad2.Draw();                                // Draw the lower pad in the canvas
    pad2.cd();                                  // pad2 becomes the current pad
    ratio->SetTitle("");                        // Turn off the title to avoid overlap
    ratio->GetXaxis()->SetLabelSize(0.12);      // Larger x-axis labels (pad is not full page)
    ratio->GetXaxis()->SetTitleSize(0.12);      // Larger x-axis title (pad is not full page)
    ratio->GetYaxis()->SetLabelSize(0.1);       // Larger y-axis labels (pad is not full page)
    ratio->GetYaxis()->SetTitleSize(0.15);      // Larger y-axis title (pad is not full page)
    ratio->GetYaxis()->SetTitle("Data/Fit");    // Change the y-axis title (this is the ratio)
    ratio->GetYaxis()->SetTitleOffset(0.3);     // Reduce the y-axis title spacing
    ratio->GetYaxis()->SetRangeUser(0.5,1.5);   // Set the y-axis ratio range from 0.5 to 1.5
    ratio->GetYaxis()->SetNdivisions(207);      // Change the y-axis tick-marks to work better
    ratio->SetMarkerStyle(3);                   // Change the marker colour to red
    ratio->SetMarkerColor(kRed);                // Change the marker colour to red
    ratio->Draw("pe");                          // Draw the ratio in the current pad

    // Add a line at 1 to the ratio plot
    TLine line(50.e3,1,200.e3,1);       // Draw a line at 1 from 50 GeV to 200 GeV (full plot)
    line.SetLineColor(kBlack);     // Set the line colour to black
    line.SetLineWidth(2);               // Set the line width to 2
    line.Draw("same");                  // Draw the line on the same plot as the ratio

    // Write the ratio plot to the output plot file
    canvas.Print(plotFileName.c_str());

    // We're done adding additional plots to the output file
    // Close the output file
    // The key is the closing square-bracket after the desired file name
    canvas.Print(Form("%s]",plotFileName.c_str()));
    
    return 0;
}

